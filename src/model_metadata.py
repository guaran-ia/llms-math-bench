"""Read model version metadata from Gemini and Azure deployment management APIs."""
from __future__ import annotations

import json
import os
import subprocess
from datetime import datetime, timezone
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _gemini_metadata(model_id: str, api_key: str) -> dict[str, Any]:
    model_name = model_id.removeprefix("models/")
    url = "https://generativelanguage.googleapis.com/v1beta/models/" + quote(model_name, safe="")
    req = Request(url, headers={"x-goog-api-key": api_key}, method="GET")
    try:
        with urlopen(req, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace").strip()
        try:
            payload = json.loads(body)
            detail = (payload.get("error") or {}).get("message") or body
        except (json.JSONDecodeError, AttributeError):
            detail = body or str(exc)
        raise RuntimeError(
            "Gemini model metadata lookup for {!r} failed (HTTP {}): {}. "
            "Check GEMINI_MODEL_ID and that GEMINI_API_KEY is enabled for the Gemini API.".format(
                model_id, exc.code, detail
            )
        ) from exc
    except (URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise RuntimeError("Gemini model metadata lookup failed for {!r}: {}".format(model_id, exc)) from exc


def _az_json(*args: str, environ: dict[str, str] | None = None) -> Any:
    env = os.environ.copy()
    if environ:
        env.update(environ)
    try:
        result = subprocess.run(
            ["az", *args, "--output", "json"], check=False,
            capture_output=True, text=True, timeout=45, env=env,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
        raise RuntimeError("Azure model metadata lookup requires Azure CLI; install it and run 'az login'.") from exc
    if result.returncode:
        message = result.stderr.strip() or result.stdout.strip() or "Azure CLI returned a failure."
        raise RuntimeError("Azure model metadata lookup failed: " + message)
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Azure CLI returned invalid JSON while looking up model metadata.") from exc


def _azure_metadata(config: dict[str, Any], environ: dict[str, str] | None = None) -> dict[str, Any]:
    env = os.environ if environ is None else environ
    host = urlparse(config["endpoint"]).hostname or ""
    account_name = host.split(".", 1)[0]
    if not account_name:
        raise RuntimeError("Cannot infer the Azure resource name from the configured endpoint.")
    subscription = env.get("AZURE_SUBSCRIPTION_ID")
    scope_args = ("--subscription", subscription) if subscription else ()
    accounts = _az_json("cognitiveservices", "account", "list", *scope_args, environ=env)
    account = next((item for item in accounts if item.get("name", "").casefold() == account_name.casefold()), None)
    if account is None:
        raise RuntimeError(
            "Azure resource {!r} was not found in the active subscription. Run 'az login', "
            "select the subscription, or set AZURE_SUBSCRIPTION_ID.".format(account_name)
        )
    resource_group = account.get("resourceGroup")
    if not resource_group:
        raise RuntimeError("Azure CLI did not return a resource group for " + account_name)
    deployment = _az_json(
        "cognitiveservices", "account", "deployment", "show",
        "--name", account_name, "--resource-group", resource_group,
        "--deployment-name", config["deployment_id"], *scope_args,
        environ=env,
    )
    model = (deployment.get("properties") or {}).get("model") or {}
    return {
        "version": model.get("version"),
        "model_name": model.get("name"),
        "model_format": model.get("format"),
        "deployment_name": deployment.get("name") or config["deployment_id"],
    }


def discover_model_metadata(
    config: dict[str, Any], api_key: str, environ: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Fetch current provider metadata before inference requests begin."""
    checked_at = utc_now()
    if config["provider"] == "gemini-api":
        metadata = _gemini_metadata(config["deployment_id"], api_key)
        source = "gemini_models_get"
        version = metadata.get("version")
        provider_model_id = metadata.get("name")
        status = "version_found" if version else "version_not_returned"
    else:
        metadata = _azure_metadata(config, environ=environ)
        source = "azure_resource_manager_deployment"
        version = metadata.get("version")
        provider_model_id = metadata.get("model_name") or metadata.get("deployment_name")
        status = "version_found" if version else "version_not_returned"
    return {
        "model_version": str(version) if version is not None else None,
        "provider_model_id": provider_model_id,
        "model_metadata_checked_at_utc": checked_at,
        "model_metadata_source": source,
        "model_metadata_status": status,
        "model_metadata": metadata,
    }
