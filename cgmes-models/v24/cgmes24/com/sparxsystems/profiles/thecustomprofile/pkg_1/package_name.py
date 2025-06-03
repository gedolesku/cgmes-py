from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"


@dataclass
class PackageName:
    class Meta:
        name = "package_name"
        namespace = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"

    base_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Class",
            "type": "Attribute",
            "required": True,
        },
    )
    package_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
