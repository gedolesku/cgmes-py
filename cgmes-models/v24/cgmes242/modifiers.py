from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Modifiers:
    class Meta:
        name = "modifiers"
        namespace = ""

    is_ordered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isOrdered",
            "type": "Attribute",
        },
    )
    changeable: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    is_navigable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isNavigable",
            "type": "Attribute",
        },
    )
    is_root: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isRoot",
            "type": "Attribute",
        },
    )
    is_leaf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isLeaf",
            "type": "Attribute",
        },
    )
