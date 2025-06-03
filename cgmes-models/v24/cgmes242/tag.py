from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Tag:
    class Meta:
        name = "tag"
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
    value: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    notes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    model_element: Optional[str] = field(
        default=None,
        metadata={
            "name": "modelElement",
            "type": "Attribute",
        },
    )
