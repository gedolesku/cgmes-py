from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"


@dataclass
class Entsoe:
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
    base_enumeration_literal: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_EnumerationLiteral",
            "type": "Attribute",
        },
    )
    base_enumeration: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Enumeration",
            "type": "Attribute",
        },
    )
