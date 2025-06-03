from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"


@dataclass
class EaDstXrefProperty:
    class Meta:
        name = "__ea_dst_xref_property"
        namespace = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"

    base_association: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Association",
            "type": "Attribute",
            "required": True,
        },
    )
    eastereo_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "__EAStereoName",
            "type": "Attribute",
            "required": True,
        },
    )
    ea_dst_xref_property: Optional[str] = field(
        default=None,
        metadata={
            "name": "__ea_dst_xref_property",
            "type": "Attribute",
            "required": True,
        },
    )
