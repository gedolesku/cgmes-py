from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"


@dataclass
class Deststyle:
    class Meta:
        name = "deststyle"
        namespace = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"

    base_property: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Property",
            "type": "Attribute",
            "required": True,
        },
    )
    deststyle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
