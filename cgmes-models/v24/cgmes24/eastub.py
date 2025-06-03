from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Eastub:
    class Meta:
        name = "EAStub"
        namespace = ""

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
    umltype: Optional[str] = field(
        default=None,
        metadata={
            "name": "UMLType",
            "type": "Attribute",
            "required": True,
        },
    )
