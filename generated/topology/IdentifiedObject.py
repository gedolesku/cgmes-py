"""Auto-generated — DO NOT EDIT BY HAND"""

from dataclasses import dataclass, field

__all__ = ["IdentifiedObject"]


@dataclass(kw_only=True)
class IdentifiedObject:
    """Auto-generated — DO NOT EDIT BY HAND"""

    mRID: str | None = field(
        default=None,
        metadata={"xpath": "@rdf:ID", "required": True},
    )
    name: str | None = field(
        default=None,
        metadata={"xpath": "cim:IdentifiedObject.name"},
    )
