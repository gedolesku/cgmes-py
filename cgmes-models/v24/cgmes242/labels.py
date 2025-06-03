from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Labels:
    class Meta:
        name = "labels"
        namespace = ""

    lb: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rb: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
