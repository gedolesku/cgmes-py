from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"


@dataclass
class EnumType:
    class Meta:
        name = "enum"
        namespace = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"

    base_enumeration_literal: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_EnumerationLiteral",
            "type": "Attribute",
            "required": True,
        },
    )
