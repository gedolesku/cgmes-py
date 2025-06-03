from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Model2:
    class Meta:
        name = "model"
        namespace = ""

    package2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    package: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    local_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "localID",
            "type": "Attribute",
        },
    )
    owner: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tpos: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    parent: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ea_localid: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ea_ele_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ea_eleType",
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
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ea_guid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
