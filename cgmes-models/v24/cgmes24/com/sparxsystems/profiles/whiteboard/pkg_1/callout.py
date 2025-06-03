from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/Whiteboard/1.0"


@dataclass
class Callout:
    class Meta:
        name = "callout"
        namespace = "http://www.sparxsystems.com/profiles/Whiteboard/1.0"

    base_association: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Association",
            "type": "Attribute",
            "required": True,
        },
    )
    direction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
