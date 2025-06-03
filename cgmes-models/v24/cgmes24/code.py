from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Code:
    class Meta:
        name = "code"
        namespace = ""

    gentype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
