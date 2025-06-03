from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Styleex:
    class Meta:
        name = "styleex"
        namespace = ""

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
