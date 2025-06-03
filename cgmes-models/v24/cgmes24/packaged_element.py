from dataclasses import dataclass, field
from typing import Optional

from cgmes24.generalization_2 import Generalization2
from cgmes24.member_end import MemberEnd
from cgmes24.nested_classifier import NestedClassifier
from cgmes24.owned_attribute import OwnedAttribute
from cgmes24.owned_comment import OwnedComment
from cgmes24.owned_end import OwnedEnd
from cgmes24.owned_literal import OwnedLiteral
from cgmes24.specification import OwnedRule


@dataclass
class PackagedElement:
    class Meta:
        name = "packagedElement"
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
    is_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isAbstract",
            "type": "Attribute",
        },
    )
    owned_comment: list[OwnedComment] = field(
        default_factory=list,
        metadata={
            "name": "ownedComment",
            "type": "Element",
        },
    )
    packaged_element: list["PackagedElement"] = field(
        default_factory=list,
        metadata={
            "name": "packagedElement",
            "type": "Element",
            "sequence": 1,
        },
    )
    owned_rule: list[OwnedRule] = field(
        default_factory=list,
        metadata={
            "name": "ownedRule",
            "type": "Element",
        },
    )
    owned_attribute: list[OwnedAttribute] = field(
        default_factory=list,
        metadata={
            "name": "ownedAttribute",
            "type": "Element",
            "sequence": 1,
        },
    )
    generalization: Optional[Generalization2] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    nested_classifier: list[NestedClassifier] = field(
        default_factory=list,
        metadata={
            "name": "nestedClassifier",
            "type": "Element",
        },
    )
    member_end_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "memberEnd",
            "type": "Attribute",
        },
    )
    member_end: list[MemberEnd] = field(
        default_factory=list,
        metadata={
            "name": "memberEnd",
            "type": "Element",
            "sequence": 1,
        },
    )
    owned_end: list[OwnedEnd] = field(
        default_factory=list,
        metadata={
            "name": "ownedEnd",
            "type": "Element",
        },
    )
    supplier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    client: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    owned_literal: list[OwnedLiteral] = field(
        default_factory=list,
        metadata={
            "name": "ownedLiteral",
            "type": "Element",
        },
    )
