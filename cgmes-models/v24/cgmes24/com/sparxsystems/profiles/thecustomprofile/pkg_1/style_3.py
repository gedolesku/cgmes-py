from dataclasses import dataclass, field
from typing import Optional, Union

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"


@dataclass
class Style3:
    class Meta:
        name = "style"
        namespace = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"

    base_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Class",
            "type": "Attribute",
        },
    )
    base_association: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Association",
            "type": "Attribute",
        },
    )
    style: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
