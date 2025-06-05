"""CGMES dataclass generation package."""

from .meta import Attribute, ClassMeta, EnumMeta, LinkData
from .parser import load_xmi, parse_xmi
from .writer import BASE_SRC, write_classes, write_enums
from .api import generate_dataclasses

__all__ = [
    "Attribute",
    "ClassMeta",
    "EnumMeta",
    "LinkData",
    "load_xmi",
    "parse_xmi",
    "write_classes",
    "write_enums",
    "generate_dataclasses",
    "BASE_SRC",
]
