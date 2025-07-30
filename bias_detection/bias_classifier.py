"""Very naive bias detection based on promotional keywords."""

from __future__ import annotations

BIAS_KEYWORDS = {
    "buy now",
    "must buy",
    "sponsored",
    "guaranteed",
    "limited time",
}


def detect_bias(text: str) -> float:
    """Return a bias score in ``[0, 1]`` based on keyword matches."""
    text_lower = text.lower()
    matches = sum(1 for kw in BIAS_KEYWORDS if kw in text_lower)
    return matches / len(BIAS_KEYWORDS)


__all__ = ["detect_bias"]
