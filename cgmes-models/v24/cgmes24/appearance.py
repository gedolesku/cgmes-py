from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Appearance:
    class Meta:
        name = "appearance"
        namespace = ""

    linemode: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    linecolor: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    linewidth: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    seqno: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    head_style: Optional[int] = field(
        default=None,
        metadata={
            "name": "headStyle",
            "type": "Attribute",
            "required": True,
        },
    )
    line_style: Optional[int] = field(
        default=None,
        metadata={
            "name": "lineStyle",
            "type": "Attribute",
            "required": True,
        },
    )
