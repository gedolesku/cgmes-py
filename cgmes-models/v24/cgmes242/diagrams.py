from dataclasses import dataclass, field

from cgmes242.diagram import Diagram


@dataclass
class Diagrams:
    class Meta:
        name = "diagrams"
        namespace = ""

    diagram: list[Diagram] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
