from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Packageproperties:
    class Meta:
        name = "packageproperties"
        namespace = ""

    version: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    xmiver: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tpos: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
