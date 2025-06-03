from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Type:
    class Meta:
        name = "type"
        namespace = ""

    multiplicity: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    aggregation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    containment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
        },
    )
