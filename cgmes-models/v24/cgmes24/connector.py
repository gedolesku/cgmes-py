from dataclasses import dataclass, field
from typing import Optional

from cgmes24.appearance import Appearance
from cgmes24.extended_properties import ExtendedProperties
from cgmes24.labels import Labels
from cgmes24.model_2 import Model2
from cgmes24.modifiers import Modifiers
from cgmes24.properties import Properties
from cgmes24.source import Source
from cgmes24.tags import Tags
from cgmes24.target import Target
from cgmes24.xrefs import Xrefs


@dataclass
class Connector:
    class Meta:
        name = "connector"
        namespace = ""

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
            "required": True,
        },
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    target: Optional[Target] = field(
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
    modifiers: Optional[Modifiers] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    parameter_substitutions: Optional[object] = field(
        default=None,
        metadata={
            "name": "parameterSubstitutions",
            "type": "Element",
        },
    )
    documentation: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    appearance: Optional[Appearance] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    labels: Optional[Labels] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    extended_properties: Optional[ExtendedProperties] = field(
        default=None,
        metadata={
            "name": "extendedProperties",
            "type": "Element",
            "required": True,
        },
    )
    style: Optional[object] = field(
        default=None,
        metadata={
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
    tags: Optional[Tags] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
