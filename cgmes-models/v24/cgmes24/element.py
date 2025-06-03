from dataclasses import dataclass, field
from typing import Optional

from cgmes24.attributes import Attributes
from cgmes24.code import Code
from cgmes24.constraints_2 import Constraints2
from cgmes24.extended_properties import ExtendedProperties
from cgmes24.flags import Flags
from cgmes24.links import Links
from cgmes24.model_2 import Model2
from cgmes24.packageproperties import Packageproperties
from cgmes24.project import Project
from cgmes24.properties import Properties
from cgmes24.style_4 import Style4
from cgmes24.tags import Tags
from cgmes24.times import Times
from cgmes24.xrefs import Xrefs


@dataclass
class Element:
    class Meta:
        name = "element"
        namespace = ""

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    scope: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    model: Optional[Model2] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    project: Optional[Project] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    code: Optional[Code] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    style: Optional[Style4] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tags: Optional[Tags] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xrefs: Optional[Xrefs] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    extended_properties: Optional[ExtendedProperties] = field(
        default=None,
        metadata={
            "name": "extendedProperties",
            "type": "Element",
        },
    )
    packageproperties: Optional[Packageproperties] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    paths: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    times: Optional[Times] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    flags: Optional[Flags] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    attributes: Optional[Attributes] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    constraints: Optional[Constraints2] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    links: Optional[Links] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    geometry: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    subject: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    seqno: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    style_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "style",
            "type": "Attribute",
        },
    )
