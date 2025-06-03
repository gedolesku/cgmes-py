from dataclasses import dataclass, field
from typing import Optional

from cgmes242.elements import Elements
from cgmes242.matrixitems import Matrixitems
from cgmes242.model_2 import Model2
from cgmes242.project import Project
from cgmes242.properties import Properties
from cgmes242.style1 import Style1
from cgmes242.style2 import Style2
from cgmes242.swimlanes import Swimlanes


@dataclass
class Diagram:
    class Meta:
        name = "diagram"
        namespace = ""

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
            "required": True,
        },
    )
    model: Optional[Model2] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    project: Optional[Project] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    style1: Optional[Style1] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    style2: Optional[Style2] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    swimlanes: Optional[Swimlanes] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    matrixitems: Optional[Matrixitems] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    extended_properties: Optional[object] = field(
        default=None,
        metadata={
            "name": "extendedProperties",
            "type": "Element",
        },
    )
    elements: Optional[Elements] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
