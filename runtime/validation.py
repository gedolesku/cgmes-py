from __future__ import annotations

"""Simple validation helpers for CGMES dataclasses."""

from dataclasses import fields
import re
from typing import Any, Dict, Iterable, List, Type


_Dataset = Dict[Type[Any], List[Any]]
_hooks: List[callable] = []


def add_hook(fn: callable) -> None:
    """Register a custom validation *fn* executed during :func:`validate`."""
    _hooks.append(fn)


def validate(dataset: _Dataset, *, strict: bool = False) -> None:
    """Validate objects in *dataset* based on field metadata."""
    if not strict:
        return
    for cls, objs in dataset.items():
        for obj in objs:
            for f in fields(cls):
                if f.metadata.get("required") and getattr(obj, f.name) is None:
                    raise ValueError(f"{cls.__name__}.{f.name} is required")
                pattern = f.metadata.get("pattern")
                value = getattr(obj, f.name)
                if pattern and value is not None:
                    if not re.match(pattern, str(value)):
                        raise ValueError(f"{cls.__name__}.{f.name} does not match {pattern}")
    for hook in _hooks:
        hook(dataset)


def resolve(dataset: _Dataset) -> None:
    """Dereference ``*_id`` fields into ``*_ref`` objects within *dataset*."""
    id_map: Dict[str, Any] = {}
    for objs in dataset.values():
        for obj in objs:
            mrid = getattr(obj, "mRID", None)
            if mrid is not None:
                id_map[f"#{mrid}"] = obj
    for cls, objs in dataset.items():
        for obj in objs:
            for f in fields(cls):
                if f.name.endswith("_id"):
                    ref_field = f.name[:-3] + "_ref"
                    target = id_map.get(getattr(obj, f.name))
                    if hasattr(obj, ref_field):
                        setattr(obj, ref_field, target)
