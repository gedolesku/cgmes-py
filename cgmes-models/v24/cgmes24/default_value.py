from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate


@dataclass
class DefaultValue:
    class Meta:
        name = "defaultValue"
        namespace = ""

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
            "required": True,
        },
    )
    value: Optional[Union[str, XmlDate]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
