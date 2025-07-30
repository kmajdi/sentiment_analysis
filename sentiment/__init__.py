"""Public sentiment analysis API."""

from .absa import analyze_sentiment_by_entity, simple_sentiment

__all__ = ["analyze_sentiment_by_entity", "simple_sentiment"]
