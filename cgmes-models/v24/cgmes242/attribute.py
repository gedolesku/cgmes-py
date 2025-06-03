from dataclasses import dataclass, field
from typing import Optional

from cgmes242.bounds import Bounds
from cgmes242.constraints_1 import Constraints1
from cgmes242.containment import Containment
from cgmes242.coords import Coords
from cgmes242.documentation_2 import Documentation2
from cgmes242.initial import Initial
from cgmes242.model_2 import Model2
from cgmes242.properties import Properties
from cgmes242.stereotype import Stereotype
from cgmes242.style_4 import Style4
from cgmes242.styleex import Styleex
from cgmes242.tags import Tags
from cgmes242.xrefs import Xrefs


@dataclass
class Attribute:
    class Meta:
        name = "attribute"
        namespace = ""

    idref: Optional[str] = field(
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
    scope: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    initial: Optional[Initial] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    documentation: Optional[Documentation2] = field(
        default=None,
        metadata={
            "type": "Element",
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
    coords: Optional[Coords] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    containment: Optional[Containment] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    stereotype: Optional[Stereotype] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    bounds: Optional[Bounds] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    options: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    style: Optional[Style4] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    styleex: Optional[Styleex] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    tags: Optional[Tags] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    constraints: Optional[Constraints1] = field(
        default=None,
        metadata={
            "name": "Constraints",
            "type": "Element",
        },
    )
    xrefs: Optional[Xrefs] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
