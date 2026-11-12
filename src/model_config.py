"""Provider routing and reproducibility configuration for the new study."""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ModelConfig:
    model_id: str
    provider: str
    default_deployment: str
    deployment_env: str
    endpoint_env: str
    default_endpoint: str
    api_version_env: str | None = None
    default_api_version: str | None = None

    def resolve(self, environ: dict[str, str] | None = None) -> dict[str, Any]:
        env = os.environ if environ is None else environ
        return {
            "model_id": self.model_id,
            "provider": self.provider,
            "deployment_id": env.get(self.deployment_env, self.default_deployment),
            "endpoint": (env.get(self.endpoint_env) or self.default_endpoint).rstrip("/"),
            "api_version": (
                (env.get(self.api_version_env) or self.default_api_version)
                if self.api_version_env else None
            ),
            "deployment_env": self.deployment_env,
        }


MODEL_CONFIGS = {
    "gemini-3.5-flash": ModelConfig(
        model_id="gemini-3.5-flash", provider="gemini-api",
        default_deployment="gemini-3.5-flash", deployment_env="GEMINI_MODEL_ID",
        endpoint_env="GEMINI_API_BASE_URL",
        default_endpoint="https://generativelanguage.googleapis.com/v1beta/openai",
    ),
    "grok-4.1": ModelConfig(
        model_id="grok-4.1", provider="azure-ai-services",
        default_deployment="grok-4-1-fast-non-reasoning", deployment_env="AZURE_GROK41_DEPLOYMENT",
        endpoint_env="AZURE_AI_SERVICES_ENDPOINT",
        default_endpoint="https://guarania-maas.services.ai.azure.com/openai/v1",
    ),
    "gpt-4o-mini": ModelConfig(
        model_id="gpt-4o-mini", provider="azure-openai",
        default_deployment="gpt-4o-mini", deployment_env="AZURE_GPT4O_MINI_DEPLOYMENT",
        endpoint_env="AZURE_OPENAI_ENDPOINT",
        default_endpoint="https://guarania-maas.cognitiveservices.azure.com/",
        api_version_env="AZURE_OPENAI_API_VERSION", default_api_version="2024-12-01-preview",
    ),
    "llama-3.3-70b": ModelConfig(
        model_id="llama-3.3-70b", provider="azure-ai-services",
        default_deployment="Llama-3.3-70B-Instruct", deployment_env="AZURE_LLAMA33_DEPLOYMENT",
        endpoint_env="AZURE_AI_SERVICES_ENDPOINT",
        default_endpoint="https://guarania-maas.services.ai.azure.com/openai/v1",
    ),
    "mistral-large-3": ModelConfig(
        model_id="mistral-large-3", provider="azure-ai-services",
        default_deployment="Mistral-Large-3", deployment_env="AZURE_MISTRAL_LARGE3_DEPLOYMENT",
        endpoint_env="AZURE_AI_SERVICES_ENDPOINT",
        default_endpoint="https://guarania-maas.services.ai.azure.com/openai/v1",
    ),
}


def resolve_models(model_ids: list[str] | None = None, environ: dict[str, str] | None = None) -> list[dict[str, Any]]:
    selected = list(MODEL_CONFIGS) if model_ids is None else model_ids
    unknown = [model_id for model_id in selected if model_id not in MODEL_CONFIGS]
    if unknown:
        raise ValueError("Unknown model(s): " + ", ".join(unknown))
    return [MODEL_CONFIGS[model_id].resolve(environ) for model_id in selected]


def create_client(config: dict[str, Any], api_key: str):
    """Create an OpenAI-compatible client with SDK retries disabled."""
    try:
        from openai import AzureOpenAI, OpenAI
    except ModuleNotFoundError as exc:
        if exc.name == "openai":
            raise RuntimeError("Install dependencies with: python -m pip install -r requirements.txt") from exc
        raise

    if config["provider"] == "azure-openai":
        return AzureOpenAI(
            api_key=api_key, azure_endpoint=config["endpoint"],
            api_version=config["api_version"], max_retries=0,
        )
    return OpenAI(api_key=api_key, base_url=config["endpoint"].rstrip("/") + "/", max_retries=0)
