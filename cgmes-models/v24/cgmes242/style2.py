from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Style2:
    class Meta:
        name = "style2"
        namespace = ""

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
