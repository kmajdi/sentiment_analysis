"""Simple rule-based sentiment logic for demonstration."""

from __future__ import annotations

from typing import Dict, Iterable


POSITIVE_WORDS = {
    "good",
    "great",
    "positive",
    "up",
    "surge",
    "rise",
    "profit",
}

NEGATIVE_WORDS = {
    "bad",
    "poor",
    "negative",
    "down",
    "drop",
    "fall",
    "loss",
}


def simple_sentiment(text: str) -> float:
    """Return a sentiment score in ``[-1, 1]`` for ``text``."""
    words = text.lower().split()
    if not words:
        return 0.0

    pos = sum(w in POSITIVE_WORDS for w in words)
    neg = sum(w in NEGATIVE_WORDS for w in words)
    return (pos - neg) / max(len(words), 1)


def analyze_sentiment_by_entity(text: str, entities: Iterable[str]) -> Dict[str, float]:
    """Return sentiment scores for each entity alias."""
    scores = {}
    for entity in entities:
        if entity.lower() in text.lower():
            scores[entity] = simple_sentiment(text)
    return scores


__all__ = ["analyze_sentiment_by_entity", "simple_sentiment"]
