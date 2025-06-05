from __future__ import annotations

from dataclasses import fields


def validate_required(obj: object) -> None:
    for f in fields(obj):
        if f.metadata.get("required") and getattr(obj, f.name) is None:
            raise ValueError(f"{obj.__class__.__name__}.{f.name} is required")
