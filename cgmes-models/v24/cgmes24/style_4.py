from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Style4:
    class Meta:
        name = "style"
        namespace = ""

    appearance: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    object_style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
