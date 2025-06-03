from dataclasses import dataclass, field
from typing import Optional

from cgmes242.annotated_element import AnnotatedElement


@dataclass
class OwnedComment:
    class Meta:
        name = "ownedComment"
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
    annotated_element_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "annotatedElement",
            "type": "Attribute",
        },
    )
    body: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    body_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "body",
            "type": "Attribute",
        },
    )
    annotated_element: list[AnnotatedElement] = field(
        default_factory=list,
        metadata={
            "name": "annotatedElement",
            "type": "Element",
        },
    )
