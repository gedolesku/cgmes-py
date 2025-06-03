from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Coords:
    class Meta:
        name = "coords"
        namespace = ""

    ordered: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    scale: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
