from dataclasses import dataclass, field
from typing import Optional

from cgmes24.constrained_element import ConstrainedElement


@dataclass
class Specification:
    class Meta:
        name = "specification"
        namespace = ""

    type_value: Optional[str] = field(
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
    body: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    owned_rule: list["OwnedRule"] = field(
        default_factory=list,
        metadata={
            "name": "ownedRule",
            "type": "Element",
        },
    )


@dataclass
class OwnedRule:
    class Meta:
        name = "ownedRule"
        namespace = ""

    type_value: Optional[str] = field(
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
        },
    )
    constrained_element: Optional[ConstrainedElement] = field(
        default=None,
        metadata={
            "name": "constrainedElement",
            "type": "Element",
        },
    )
    specification: Optional[Specification] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
