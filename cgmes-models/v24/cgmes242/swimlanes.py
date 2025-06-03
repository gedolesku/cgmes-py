from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Swimlanes:
    class Meta:
        name = "swimlanes"
        namespace = ""

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
