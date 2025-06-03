from dataclasses import dataclass, field
from typing import Optional

from cgmes242.constraint_1 import Constraint1


@dataclass
class Constraints1:
    class Meta:
        name = "Constraints"
        namespace = ""

    constraint: Optional[Constraint1] = field(
        default=None,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "required": True,
        },
    )
