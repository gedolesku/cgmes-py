from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"


@dataclass
class VirtualInheritance:
    class Meta:
        name = "virtualInheritance"
        namespace = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"

    base_association: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Association",
            "type": "Attribute",
            "required": True,
        },
    )
    virtual_inheritance: Optional[int] = field(
        default=None,
        metadata={
            "name": "virtualInheritance",
            "type": "Attribute",
            "required": True,
        },
    )
