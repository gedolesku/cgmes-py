from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Containment:
    class Meta:
        name = "containment"
        namespace = ""

    containment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
