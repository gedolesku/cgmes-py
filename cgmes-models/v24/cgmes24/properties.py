from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Properties:
    class Meta:
        name = "properties"
        namespace = ""

    documentation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    is_specification: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isSpecification",
            "type": "Attribute",
        },
    )
    s_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "sType",
            "type": "Attribute",
        },
    )
    n_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "nType",
            "type": "Attribute",
        },
    )
    alias: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    scope: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ea_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    stereotype: Optional[str] = field(
        default=None,
        metadata={
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
    is_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isAbstract",
            "type": "Attribute",
        },
    )
    is_active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isActive",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    derived: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    precision: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    collection: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    length: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    static: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    duplicates: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    changeability: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    subtype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    direction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
