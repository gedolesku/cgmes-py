from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ExtendedProperties:
    class Meta:
        name = "extendedProperties"
        namespace = ""

    tagged: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    package_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    relatedlinks: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ea_attsclassified: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cardinality: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    conditional: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    virtual_inheritance: Optional[int] = field(
        default=None,
        metadata={
            "name": "virtualInheritance",
            "type": "Attribute",
        },
    )
