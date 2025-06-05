from __future__ import annotations

"""Simple validation helpers for CGMES dataclasses."""

from dataclasses import fields
from typing import Any, Iterable, Callable, List
import re


_HOOKS: List[Callable[[Any], None]] = []


def add_hook(fn: Callable[[Any], None]) -> None:
    """Register a validation hook executed after built-in checks."""

    _HOOKS.append(fn)


def _validate_fields(obj: Any) -> None:
    """Check ``required`` and ``pattern`` metadata on *obj* fields."""

    for f in fields(obj):
        meta = f.metadata
        value = getattr(obj, f.name)
        if meta.get("required") and value is None:
            raise ValueError(f"{type(obj).__name__}.{f.name} is required")
        pattern = meta.get("pattern")
        if pattern and value is not None and not re.match(pattern, str(value)):
            raise ValueError(f"{type(obj).__name__}.{f.name} does not match {pattern}")


def _topologicalnode_ids(dataset: Iterable[Any]) -> set[str]:
    ids = set()
    for item in dataset:
        if type(item).__name__ == "TopologicalNode":
            node_id = getattr(item, "mRID", None) or getattr(item, "id", None)
            if node_id:
                ids.add(node_id)
    return ids


def validate_semantics(
    obj: Any, *, dataset: Iterable[Any] | None = None, profile: str | None = None
) -> None:
    """Perform basic semantic checks on *obj*.

    Parameters
    ----------
    obj:
        Dataclass instance to validate.
    dataset:
        Iterable of additional objects used for cross-reference checks.
    profile:
        Dataset profile such as ``"EQ"`` or ``"SSH"``.
    """

    cls = type(obj).__name__
    if cls == "SvVoltage":
        tn_id = getattr(obj, "TopologicalNode_id", None)
        if not tn_id:
            raise ValueError("SvVoltage.TopologicalNode_id is required")
        if dataset is not None:
            if tn_id not in _topologicalnode_ids(dataset):
                raise ValueError(f"SvVoltage.TopologicalNode_id '{tn_id}' not found")

    if cls == "ConnectivityNode":
        tn_id = getattr(obj, "TopologicalNode_id", None)
        if profile == "SSH" and not tn_id:
            raise ValueError("ConnectivityNode.TopologicalNode_id is required in SSH")


def validate(
    obj: Any,
    *,
    strict: bool = True,
    semantic: bool = True,
    dataset: Iterable[Any] | None = None,
    profile: str | None = None,
) -> None:
    """Run built-in validators for *obj*.

    ``strict`` enables ``required``/``pattern`` checks. ``semantic`` triggers
    cross-object rules such as :func:`validate_semantics`.
    """

    if strict:
        _validate_fields(obj)
    if semantic:
        validate_semantics(obj, dataset=dataset, profile=profile)
    for hook in _HOOKS:
        hook(obj)
