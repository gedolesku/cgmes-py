from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Project:
    class Meta:
        name = "project"
        namespace = ""

    author: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[Union[float, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    phase: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    created: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    modified: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    complexity: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
