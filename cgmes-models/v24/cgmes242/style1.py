from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Style1:
    class Meta:
        name = "style1"
        namespace = ""

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
