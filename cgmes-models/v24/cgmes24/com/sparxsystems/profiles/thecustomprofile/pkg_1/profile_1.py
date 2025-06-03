from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"


@dataclass
class Profile1:
    class Meta:
        name = "Profile"
        namespace = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"

    base_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Class",
            "type": "Attribute",
            "required": True,
        },
    )
    profile: Optional[str] = field(
        default=None,
        metadata={
            "name": "Profile",
            "type": "Attribute",
            "required": True,
        },
    )
