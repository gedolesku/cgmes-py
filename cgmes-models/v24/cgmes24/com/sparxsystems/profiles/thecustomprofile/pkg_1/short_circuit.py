from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"


@dataclass
class ShortCircuit:
    class Meta:
        namespace = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"

    base_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Class",
            "type": "Attribute",
        },
    )
    base_property: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Property",
            "type": "Attribute",
        },
    )
