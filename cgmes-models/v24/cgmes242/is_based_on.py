from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"


@dataclass
class IsBasedOn:
    class Meta:
        namespace = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"

    base_dependency: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Dependency",
            "type": "Attribute",
            "required": True,
        },
    )
