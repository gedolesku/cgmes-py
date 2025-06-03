from dataclasses import dataclass, field

from cgmes242.attribute import Attribute


@dataclass
class Attributes:
    class Meta:
        name = "attributes"
        namespace = ""

    attribute: list[Attribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
