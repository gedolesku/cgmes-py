from __future__ import annotations

from functools import wraps
from pathlib import Path
from typing import Iterator, Type, TypeVar

from lxml import etree

from .base import parse_dataclass, parse_file as _parse_file, parse_dataset, to_element
from .exporter import export_dataset
from . import validation

T = TypeVar("T")


@wraps(parse_dataclass)
def _parse_element(elem: etree._Element, cls: Type[T]) -> T:
    obj = parse_dataclass(elem, cls)
    validation.validate({cls: [obj]}, strict=True)
    validation.resolve({cls: [obj]})
    return obj


@wraps(_parse_file)
def parse_file(source: str | Path | etree._Element, cls: Type[T]) -> Iterator[T] | T:
    """Parse *source* into ``cls`` objects with strict validation."""
    if isinstance(source, etree._Element):
        return _parse_element(source, cls)
    data = parse_dataset(str(source), [cls])[cls]
    return iter(data)


parse_file.__wrapped__ = _parse_element


__all__ = [
    "parse_file",
    "parse_dataset",
    "to_element",
    "parse_dataclass",
    "export_dataset",
]
