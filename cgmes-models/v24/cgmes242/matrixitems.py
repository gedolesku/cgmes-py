from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Matrixitems:
    class Meta:
        name = "matrixitems"
        namespace = ""

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
