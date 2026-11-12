"""Read Gemini model metadata and Azure versions supplied from the portal."""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from urllib.parse import quote


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


def _azure_metadata(config: dict[str, Any]) -> dict[str, Any]:
    """Use the model version copied from the Azure deployment Details page."""
    return {
        "version": config.get("model_version"),
        "model_name": config.get("model_id"),
        "deployment_name": config.get("deployment_id"),
    }


def discover_model_metadata(
    config: dict[str, Any], api_key: str = "", environ: dict[str, str] | None = None,
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
        metadata = _azure_metadata(config)
        source = "azure_portal_configuration"
        version = metadata.get("version")
        provider_model_id = metadata.get("model_name") or metadata.get("deployment_name")
        status = "version_configured" if version else "version_not_configured"
    return {
        "model_version": str(version) if version is not None else None,
        "provider_model_id": provider_model_id,
        "model_metadata_checked_at_utc": checked_at,
        "model_metadata_portal_checked_at_utc": (
            (environ if environ is not None else os.environ).get("AZURE_MODEL_METADATA_PORTAL_CHECKED_AT_UTC") or None
            if config["provider"] != "gemini-api" else None
        ),
        "model_metadata_source": source,
        "model_metadata_status": status,
        "model_metadata": metadata,
    }
