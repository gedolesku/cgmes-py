from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Documentation2:
    class Meta:
        name = "documentation"
        namespace = ""

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
