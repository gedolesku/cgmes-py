from dataclasses import dataclass, field
from typing import Optional

from cgmes242.default_value import DefaultValue
from cgmes242.lower_value import LowerValue
from cgmes242.type_mod import Type
from cgmes242.upper_value import UpperValue


@dataclass
class OwnedAttribute:
    class Meta:
        name = "ownedAttribute"
        namespace = ""

    type_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    is_static: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isStatic",
            "type": "Attribute",
        },
    )
    is_read_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isReadOnly",
            "type": "Attribute",
        },
    )
    association: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[Type] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    lower_value: Optional[LowerValue] = field(
        default=None,
        metadata={
            "name": "lowerValue",
            "type": "Element",
        },
    )
    upper_value: Optional[UpperValue] = field(
        default=None,
        metadata={
            "name": "upperValue",
            "type": "Element",
        },
    )
    default_value: Optional[DefaultValue] = field(
        default=None,
        metadata={
            "name": "defaultValue",
            "type": "Element",
        },
    )
