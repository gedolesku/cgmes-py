from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"


@dataclass
class GuidbasedOn:
    class Meta:
        name = "GUIDBasedOn"
        namespace = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"

    base_property: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Property",
            "type": "Attribute",
        },
    )
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
    base_generalization: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Generalization",
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
    guidbased_on: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDBasedOn",
            "type": "Attribute",
            "required": True,
        },
    )
