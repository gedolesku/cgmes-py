from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Xrefs:
    class Meta:
        name = "xrefs"
        namespace = ""

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
