from dataclasses import dataclass, field

from cgmes24.constraint_2 import Constraint2


@dataclass
class Constraints2:
    class Meta:
        name = "constraints"
        namespace = ""

    constraint: list[Constraint2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
