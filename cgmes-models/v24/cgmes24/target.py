from dataclasses import dataclass, field
from typing import Optional

from cgmes24.documentation_2 import Documentation2
from cgmes24.model_2 import Model2
from cgmes24.modifiers import Modifiers
from cgmes24.role import Role
from cgmes24.style_4 import Style4
from cgmes24.tags import Tags
from cgmes24.type_mod import Type
from cgmes24.xrefs import Xrefs


@dataclass
class Target:
    class Meta:
        name = "target"
        namespace = ""

    idref: Optional[str] = field(
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
    role: Optional[Role] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
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
    constraints: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    modifiers: Optional[Modifiers] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    style: Optional[Style4] = field(
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
