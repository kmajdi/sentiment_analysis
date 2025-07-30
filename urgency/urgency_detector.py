"""Simple urgency detection using keyword spotting."""

from __future__ import annotations

URGENCY_KEYWORDS = {
    "breaking",
    "urgent",
    "immediately",
    "right now",
    "shortly",
}


def detect_urgency(text: str) -> float:
    """Return an urgency score in ``[0, 1]``."""
    text_lower = text.lower()
    matches = sum(1 for kw in URGENCY_KEYWORDS if kw in text_lower)
    return matches / len(URGENCY_KEYWORDS)


__all__ = ["detect_urgency"]
