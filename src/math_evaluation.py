"""Shared, conservative answer parsing and mathematical equivalence checks."""
from __future__ import annotations

import json
import re
from decimal import Decimal, InvalidOperation
from typing import Any

try:
    import sympy as sp
except ImportError:  # Numeric and structural evaluation remains available.
    sp = None


def parse_numeric(value: Any) -> Decimal | None:
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float, Decimal)):
        try:
            result = Decimal(str(value))
        except InvalidOperation:
            return None
        return result if result.is_finite() else None
    if isinstance(value, str):
        candidate = value.strip().replace(",", ".")
        if not re.fullmatch(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", candidate):
            return None
        try:
            result = Decimal(candidate)
        except InvalidOperation:
            return None
        return result if result.is_finite() else None
    return None


def extract_json(raw: str | None) -> Any:
    if not isinstance(raw, str) or not raw.strip():
        return None
    text = raw.strip()
    fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", text, re.I | re.S)
    if fenced:
        text = fenced.group(1).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Accept a single JSON object surrounded by prose, while still requiring
        # the final answer to come from its explicit final_answer field.
        start, end = text.find("{"), text.rfind("}")
        if start < 0 or end <= start:
            return None
        try:
            return json.loads(text[start:end + 1])
        except json.JSONDecodeError:
            return None


def final_value(response: Any) -> Any:
    if isinstance(response, (int, float, Decimal)) and not isinstance(response, bool):
        return response
    if isinstance(response, str) and parse_numeric(response) is not None:
        return response
    if not isinstance(response, dict):
        return None
    value = response.get("final_answer")
    if isinstance(value, dict):
        return value.get("value")
    return value


def _sympy_expr(value: Any):
    if sp is None or not isinstance(value, str):
        return None
    text = value.strip().replace("²", "**2").replace("√", "sqrt")
    text = text.replace("−", "-").replace("×", "*").replace("÷", "/")
    if not text or len(text) > 500 or not re.fullmatch(r"[A-Za-z0-9\s.+\-*/^=(),]*", text):
        return None
    if any(len(token) > 20 for token in re.findall(r"[A-Za-z][A-Za-z0-9]*", text)):
        return None
    if any(len(token) > 30 for token in re.findall(r"\d+", text)):
        return None
    text = text.replace("^", "**")
    if any(abs(int(power)) > 100 for power in re.findall(r"\*\*\s*(-?\d+)", text)):
        return None
    identifiers = set(re.findall(r"[A-Za-z][A-Za-z0-9]*", text))
    local_symbols = {name: sp.Symbol(name) for name in identifiers - {"sqrt", "pi", "E"}}
    local_symbols.update({"sqrt": sp.sqrt, "pi": sp.pi, "E": sp.E})
    try:
        if "=" in text:
            left, right = text.split("=", 1)
            return sp.simplify(sp.sympify(left, locals=local_symbols) - sp.sympify(right, locals=local_symbols))
        return sp.simplify(sp.sympify(text, locals=local_symbols))
    except (sp.SympifyError, TypeError, ValueError, SyntaxError):
        return None


def equivalent(expected: Any, actual: Any, tolerance: Decimal = Decimal("0.0001")) -> bool:
    if isinstance(expected, bool) or isinstance(actual, bool):
        return expected is actual
    if (isinstance(expected, (int, float, Decimal)) or parse_numeric(expected) is not None
            or parse_numeric(actual) is not None):
        left, right = parse_numeric(expected), parse_numeric(actual)
        if left is not None and right is not None:
            return abs(left - right) <= tolerance
        if sp is not None:
            a, b = _sympy_expr(str(expected)), _sympy_expr(actual)
            return a is not None and b is not None and sp.simplify(a - b) == 0
        return False
    if isinstance(expected, list):
        if isinstance(actual, str):
            numbers = re.findall(r"[+-]?(?:\d+(?:[.,]\d*)?|[.,]\d+)", actual)
            actual = numbers if len(numbers) == len(expected) else actual
        return isinstance(actual, list) and len(expected) == len(actual) and all(
            equivalent(a, b, tolerance) for a, b in zip(expected, actual)
        )
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            return False
        aliases = {"center": ("center", "centro", "isentro", "iséntro"), "radius": ("radius", "radio", "irradio", "irádio")}
        normalized = {str(k).casefold().replace("ó", "o"): v for k, v in actual.items()}
        for key, value in expected.items():
            candidate = normalized.get(key.casefold())
            if candidate is None and key in aliases:
                candidate = next((normalized.get(alias.replace("ó", "o")) for alias in aliases[key] if normalized.get(alias.replace("ó", "o")) is not None), None)
            if candidate is None or not equivalent(value, candidate, tolerance):
                return False
        return True
    if isinstance(expected, str) and isinstance(actual, str):
        a, b = _sympy_expr(expected), _sympy_expr(actual)
        if a is not None and b is not None:
            return sp.simplify(a - b) == 0
        return re.sub(r"\s+", "", expected).casefold() == re.sub(r"\s+", "", actual).casefold()
    return expected == actual


def evaluate(row: dict[str, Any]) -> dict[str, Any]:
    parsed = row.get("response")
    recovered = parsed if parsed is not None else extract_json(row.get("raw_response"))
    if recovered is None:
        # Only accept an entire raw response that is itself a number. Never
        # mine a number out of explanatory prose.
        recovered = parse_numeric(row.get("raw_response"))
    predicted = final_value(recovered)
    return {
        "correct": row.get("error") is None and equivalent(row.get("expected_answer"), predicted),
        "predicted": predicted,
        "json_valid": isinstance(parsed, dict) and row.get("json_parse_error") is None,
    }
