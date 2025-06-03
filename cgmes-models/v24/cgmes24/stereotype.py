from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Stereotype:
    class Meta:
        name = "stereotype"
        namespace = ""

    stereotype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
