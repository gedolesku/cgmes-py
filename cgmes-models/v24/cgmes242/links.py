from dataclasses import dataclass, field

from cgmes242.aggregation import Aggregation
from cgmes242.association import Association
from cgmes242.dependency import Dependency
from cgmes242.generalization_1 import Generalization1
from cgmes242.note_link import NoteLink


@dataclass
class Links:
    class Meta:
        name = "links"
        namespace = ""

    association: list[Association] = field(
        default_factory=list,
        metadata={
            "name": "Association",
            "type": "Element",
        },
    )
    generalization: list[Generalization1] = field(
        default_factory=list,
        metadata={
            "name": "Generalization",
            "type": "Element",
        },
    )
    dependency: list[Dependency] = field(
        default_factory=list,
        metadata={
            "name": "Dependency",
            "type": "Element",
        },
    )
    aggregation: list[Aggregation] = field(
        default_factory=list,
        metadata={
            "name": "Aggregation",
            "type": "Element",
            "sequence": 1,
        },
    )
    note_link: list[NoteLink] = field(
        default_factory=list,
        metadata={
            "name": "NoteLink",
            "type": "Element",
            "sequence": 1,
        },
    )
