from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Role:
    class Meta:
        name = "role"
        namespace = ""

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    stereotype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    visibility: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    target_scope: Optional[str] = field(
        default=None,
        metadata={
            "name": "targetScope",
            "type": "Attribute",
        },
    )
