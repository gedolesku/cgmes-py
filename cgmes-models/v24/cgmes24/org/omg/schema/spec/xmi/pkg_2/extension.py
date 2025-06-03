from dataclasses import dataclass, field
from typing import Optional

from cgmes24.connectors import Connectors
from cgmes24.diagrams import Diagrams
from cgmes24.eastub import Eastub
from cgmes24.elements import Elements
from cgmes24.images import Images
from cgmes24.primitivetypes import Primitivetypes
from cgmes24.profiles import Profiles

__NAMESPACE__ = "http://schema.omg.org/spec/XMI/2.1"


@dataclass
class Extension:
    class Meta:
        namespace = "http://schema.omg.org/spec/XMI/2.1"

    extender: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    extender_id: Optional[float] = field(
        default=None,
        metadata={
            "name": "extenderID",
            "type": "Attribute",
            "required": True,
        },
    )
    elements: Optional[Elements] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    connectors: Optional[Connectors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    primitivetypes: Optional[Primitivetypes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    profiles: Optional[Profiles] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    diagrams: Optional[Diagrams] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    eastub: list[Eastub] = field(
        default_factory=list,
        metadata={
            "name": "EAStub",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    images: Optional[Images] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
