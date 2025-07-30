"""Entity linking API."""

from .ner import detect_entities
from .linker import load_mapping_table, link_entities

__all__ = ["detect_entities", "load_mapping_table", "link_entities"]
