from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ConstrainedElement:
    class Meta:
        name = "constrainedElement"
        namespace = ""

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
            "required": True,
        },
    )
