from dataclasses import dataclass, field
from typing import Optional

from cgmes24.lower_value import LowerValue
from cgmes24.type_mod import Type
from cgmes24.upper_value import UpperValue


@dataclass
class OwnedEnd:
    class Meta:
        name = "ownedEnd"
        namespace = ""

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
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
    association: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    aggregation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_1: Optional[Type] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
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
    type_2: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    is_composite: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isComposite",
            "type": "Attribute",
        },
    )
    lower: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    upper: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    member_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "memberEnd",
            "type": "Attribute",
        },
    )
