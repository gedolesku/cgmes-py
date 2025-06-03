from dataclasses import dataclass, field

from cgmes242.element import Element


@dataclass
class Elements:
    class Meta:
        name = "elements"
        namespace = ""

    element: list[Element] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
