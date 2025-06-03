from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Flags:
    class Meta:
        name = "flags"
        namespace = ""

    iscontrolled: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    isprotected: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    batchsave: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    batchload: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    usedtd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    logxml: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    package_flags: Optional[str] = field(
        default=None,
        metadata={
            "name": "packageFlags",
            "type": "Attribute",
        },
    )
