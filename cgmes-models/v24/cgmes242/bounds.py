from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Bounds:
    class Meta:
        name = "bounds"
        namespace = ""

    lower: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    upper: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
