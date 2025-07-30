"""Very small NER helper based on simple string matching."""

from __future__ import annotations

from typing import Iterable, List


def detect_entities(text: str, aliases: Iterable[str]) -> List[str]:
    """Return all aliases found in ``text``."""
    found = []
    text_lower = text.lower()
    for alias in aliases:
        if alias.lower() in text_lower:
            found.append(alias)
    # Deduplicate while preserving order
    seen = set()
    unique = []
    for a in found:
        if a.lower() not in seen:
            unique.append(a)
            seen.add(a.lower())
    return unique


__all__ = ["detect_entities"]
