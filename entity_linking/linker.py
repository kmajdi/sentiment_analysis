"""Utility functions for mapping detected entities to stock tickers."""

from __future__ import annotations

from typing import Dict, Iterable

import pandas as pd


def load_mapping_table(path: str) -> pd.DataFrame:
    """Load the mapping CSV file."""
    return pd.read_csv(path)


def link_entities(entities: Iterable[str], mapping_df: pd.DataFrame) -> Dict[str, str]:
    """Map aliases to tickers using ``mapping_df``.

    Returns a dictionary ``alias -> ticker`` for matches found in ``mapping_df``.
    """

    result: Dict[str, str] = {}
    for alias in entities:
        mask = mapping_df["Alias/Name"].str.lower() == alias.lower()
        if mask.any():
            ticker = mapping_df.loc[mask, "Ticker"].iloc[0]
            result[alias] = ticker
    return result


__all__ = ["load_mapping_table", "link_entities"]
