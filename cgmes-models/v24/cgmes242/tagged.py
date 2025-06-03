from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"


@dataclass
class Tagged:
    class Meta:
        name = "tagged"
        namespace = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"

    base_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Class",
            "type": "Attribute",
            "required": True,
        },
    )
    tagged: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
