"""Utility helpers for the sentiment analysis project."""

from __future__ import annotations

import pandas as pd
import yaml


def load_config(path: str) -> dict:
    """Load a YAML configuration file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_mapping_table(path: str) -> pd.DataFrame:
    """Load the alias to ticker mapping table."""
    return pd.read_csv(path)


def clean_text(text: str) -> str:
    """Collapse whitespace in ``text``."""
    return " ".join(text.split())


__all__ = ["load_config", "load_mapping_table", "clean_text"]
