from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"


@dataclass
class Sourcestyle:
    class Meta:
        name = "sourcestyle"
        namespace = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"

    base_property: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Property",
            "type": "Attribute",
            "required": True,
        },
    )
    sourcestyle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
