"""Run the fresh crossed Guarani/Spanish mathematical reasoning study."""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from src.dataset import DATASETS, LANGUAGES, PROJECT_ROOT, load_dataset, problem_text
from src.model_config import MODEL_CONFIGS, create_client
from src.model_metadata import discover_model_metadata
from src.prompting import CONDITIONS, PROMPTS_PATH, render_prompt

DEFAULT_TEMPERATURE = 0.0
DEFAULT_MAX_TOKENS = 2048


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def run_id_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("\"'").strip())


def read_api_key(config: dict[str, Any]) -> str:
    names = ("GEMINI_API_KEY",) if config["provider"] == "gemini-api" else ("AZURE_OPENAI_API_KEY",)
    for name in names:
        if os.getenv(name):
            return os.environ[name]
    raise RuntimeError("Missing API credential in environment: " + " or ".join(names))


def planned_call_count(dataset_ids, model_ids, languages, condition_ids) -> int:
    return sum(len(load_dataset(dataset_id)[0]) for dataset_id in dataset_ids) * len(model_ids) * len(languages) * len(condition_ids)


def _model_version(client, config, response) -> str | None:
    returned = getattr(response, "model", None)
    if returned:
        return str(returned)
    return config.get("model_version")


def _dump_usage(response) -> Any:
    usage = getattr(response, "usage", None)
    if usage is None:
        return None
    if hasattr(usage, "model_dump"):
        return usage.model_dump(exclude_none=True)
    if hasattr(usage, "dict"):
        return usage.dict(exclude_none=True)
    return str(usage)


def _parse_json(content: str | None):
    if not content:
        return None, "empty_response"
    try:
        return json.loads(content), None
    except (json.JSONDecodeError, TypeError) as exc:
        return None, str(exc)


def _request(client, deployment_id: str, prompt: str, temperature: float, max_tokens: int):
    return client.chat.completions.create(
        model=deployment_id,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )


def _api_key_env(provider: str) -> str:
    return "GEMINI_API_KEY" if provider == "gemini-api" else "AZURE_OPENAI_API_KEY"


def _credential_name(config: dict[str, Any]) -> str:
    return _api_key_env(config["provider"])


def run(args) -> Path | None:
    load_dotenv(PROJECT_ROOT / ".env")
    dataset_ids = args.datasets or list(DATASETS)
    model_ids = args.models or list(MODEL_CONFIGS)
    languages = args.languages or list(LANGUAGES)
    condition_ids = args.conditions or list(CONDITIONS)
    for condition_id in condition_ids:
        if condition_id not in CONDITIONS:
            raise ValueError("Unknown prompt condition: " + condition_id)

    selections = {}
    for dataset_id in dataset_ids:
        rows, path = load_dataset(dataset_id)
        selections[dataset_id] = (rows, path, sha256_file(path))
        # Fail before making any paid calls if any requested cell cannot be rendered.
        for row in rows:
            for language in languages:
                text = problem_text(row, language)
                for condition_id in condition_ids:
                    render_prompt(condition_id, language, text, row)

    model_configs = [MODEL_CONFIGS[model_id].resolve() for model_id in model_ids]
    call_count = sum(len(item[0]) for item in selections.values()) * len(model_configs) * len(languages) * len(condition_ids)
    run_id = run_id_now()
    output_path = Path(args.output) if args.output else PROJECT_ROOT / "results" / ("run_" + run_id + ".jsonl")
    if not output_path.is_absolute():
        output_path = PROJECT_ROOT / output_path

    if args.check_model_metadata:
        metadata_rows = []
        for config in model_configs:
            key = _credential_name(config)
            api_key = os.getenv(key)
            if not api_key:
                raise RuntimeError("Set " + key + " in .env or the environment before checking model metadata.")
            config.update(discover_model_metadata(config, api_key))
            metadata_rows.append({
                "model_id": config["model_id"],
                "deployment_id": config["deployment_id"],
                "model_version": config.get("model_version"),
                "provider_model_id": config.get("provider_model_id"),
                "checked_at_utc": config.get("model_metadata_checked_at_utc"),
                "source": config.get("model_metadata_source"),
                "status": config.get("model_metadata_status"),
            })
        print(json.dumps({"metadata_only": True, "paid_api_calls": 0, "models": metadata_rows}, ensure_ascii=False, indent=2))
        return None

    if args.dry_run:
        summary = {
            "run_id": run_id,
            "planned_model_requests": call_count,
            "datasets": {key: len(value[0]) for key, value in selections.items()},
            "models": [dict(model_id=x["model_id"], provider=x["provider"], deployment_id=x["deployment_id"]) for x in model_configs],
            "languages": languages,
            "prompt_conditions": condition_ids,
            "output": str(output_path),
            "paid_api_calls": 0,
        }
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        if args.show_prompts:
            first_dataset = dataset_ids[0]
            first_problem = selections[first_dataset][0][0]
            print("\n--- PROMPT PREVIEWS ---")
            for language in languages:
                for condition_id in condition_ids:
                    txt = problem_text(first_problem, language)
                    print("\n### {} / {}\n{}".format(language, condition_id, render_prompt(condition_id, language, txt, first_problem)))
        return None

    clients = {}
    credentials = {}
    for config in model_configs:
        key = _credential_name(config)
        api_key = os.getenv(key)
        if not api_key:
            raise RuntimeError("Set " + key + " in .env or the environment before running model calls.")
        credentials[config["model_id"]] = api_key
    # Read-only provider metadata is resolved before any inference requests.
    for config in model_configs:
        metadata = discover_model_metadata(config, credentials[config["model_id"]])
        config.update(metadata)
        print("Model metadata: {} version={} status={} checked_at={}".format(
            config["model_id"], config.get("model_version") or "not exposed",
            config["model_metadata_status"], config["model_metadata_checked_at_utc"],
        ))
        clients[config["model_id"]] = create_client(config, credentials[config["model_id"]])

    output_path.parent.mkdir(parents=True, exist_ok=True)
    sdk_version = importlib.metadata.version("openai")
    print("Starting {} model requests. Output: {}".format(call_count, output_path))
    completed = 0
    with output_path.open("x", encoding="utf-8") as sink:
        for dataset_id in dataset_ids:
            rows, dataset_path, dataset_hash = selections[dataset_id]
            for row in rows:
                for language in languages:
                    text = problem_text(row, language)
                    for condition_id in condition_ids:
                        prompt = render_prompt(condition_id, language, text, row)
                        prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
                        for config in model_configs:
                            requested_at = utc_now()
                            started = time.monotonic()
                            raw_response = None
                            parsed_response = None
                            parse_error = None
                            error = None
                            response = None
                            finish_reason = None
                            response_id = None
                            fingerprint = None
                            try:
                                response = _request(
                                    clients[config["model_id"]], config["deployment_id"],
                                    prompt, args.temperature, args.max_tokens,
                                )
                                choice = response.choices[0]
                                raw_response = choice.message.content
                                finish_reason = getattr(choice, "finish_reason", None)
                                parsed_response, parse_error = _parse_json(raw_response)
                                response_id = getattr(response, "id", None)
                                fingerprint = getattr(response, "system_fingerprint", None)
                            except Exception as exc:  # Keep one failed attempt as a result; never retry silently.
                                error = "{}: {}".format(type(exc).__name__, str(exc))
                            finished_at = utc_now()
                            result = {
                                "schema_version": "1.0",
                                "run_id": run_id,
                                "request_id": str(uuid.uuid4()),
                                "dataset_id": dataset_id,
                                "dataset_name": DATASETS[dataset_id]["name"],
                                "dataset_level": DATASETS[dataset_id]["level"],
                                "dataset_path": str(dataset_path.relative_to(PROJECT_ROOT)),
                                "dataset_sha256": dataset_hash,
                                "problem_id": row.get("id"),
                                "problem_text": text,
                                "expected_answer": row.get("expected_answer"),
                                "reasoning_type_id": row.get("reasoning_type_id"),
                                "language": language,
                                "prompt_condition_id": condition_id,
                                "prompt_name": CONDITIONS[condition_id]["name"],
                                "prompt_set_version": PROMPT_SET_VERSION,
                                "prompts_file_sha256": sha256_file(PROMPTS_PATH),
                                "rendered_prompt_sha256": prompt_hash,
                                "model_id": config["model_id"],
                                "deployment_id": config["deployment_id"],
                                "configured_model_version": config.get("model_version"),
                                "model_metadata_provider_model_id": config.get("provider_model_id"),
                                "model_metadata_source": config.get("model_metadata_source"),
                                "model_metadata_status": config.get("model_metadata_status"),
                                "model_metadata": config.get("model_metadata"),
                                "provider_returned_model_id": _model_version(clients[config["model_id"]], config, response) if response is not None else None,
                                "model_metadata_checked_at_utc": config.get("model_metadata_checked_at_utc"),
                                "provider": config["provider"],
                                "endpoint": config["endpoint"],
                                "api_version": config.get("api_version"),
                                "accessed_at_utc": requested_at,
                                "completed_at_utc": finished_at,
                                "api_settings": {
                                    "temperature": args.temperature,
                                    "max_tokens": args.max_tokens,
                                    "response_format": "prompt_enforced_json",
                                    "sdk_retries": 0,
                                },
                                "sdk": {"name": "openai-python", "version": sdk_version, "python": platform.python_version()},
                                "response_id": response_id,
                                "finish_reason": finish_reason,
                                "system_fingerprint": fingerprint,
                                "usage": _dump_usage(response) if response is not None else None,
                                "latency_seconds": round(time.monotonic() - started, 3),
                                "response": parsed_response,
                                "raw_response": raw_response,
                                "json_parse_error": parse_error,
                                "error": error,
                            }
                            sink.write(json.dumps(result, ensure_ascii=False) + "\n")
                            sink.flush()
                            completed += 1
                            print("{}/{} {}:{} {} {} {}".format(
                                completed, call_count, dataset_id, row.get("id"), language,
                                condition_id, config["model_id"],
                            ), end="\r", flush=True)
    print("\nFinished run {}".format(run_id))
    return output_path


PROMPT_SET_VERSION = "guarani-math-prompt-set-1.0"


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--datasets", nargs="+", choices=list(DATASETS))
    parser.add_argument("--models", nargs="+", choices=list(MODEL_CONFIGS))
    parser.add_argument("--languages", nargs="+", choices=list(LANGUAGES))
    parser.add_argument("--conditions", nargs="+", choices=list(CONDITIONS))
    parser.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE)
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    parser.add_argument("--output", help="JSONL output path; default is a unique timestamped file directly under results/.")
    checks = parser.add_mutually_exclusive_group()
    checks.add_argument("--dry-run", action="store_true", help="Validate the full matrix and report planned calls without reading API keys or calling providers.")
    checks.add_argument("--check-model-metadata", action="store_true", help="Read model versions from provider metadata APIs without sending inference requests.")
    parser.add_argument("--show-prompts", action="store_true", help="With --dry-run, print prompt previews for each selected language and condition.")
    return parser.parse_args(argv)


if __name__ == "__main__":
    run(parse_args())
