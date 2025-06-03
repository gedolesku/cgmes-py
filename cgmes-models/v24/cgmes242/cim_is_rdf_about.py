from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"


@dataclass
class CimIsRdfAbout:
    class Meta:
        name = "CIM_IsRdfAbout"
        namespace = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"

    base_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Class",
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
    cim_is_rdf_about: Optional[str] = field(
        default=None,
        metadata={
            "name": "CIM_IsRdfAbout",
            "type": "Attribute",
            "required": True,
        },
    )
