from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate


@dataclass
class Initial:
    class Meta:
        name = "initial"
        namespace = ""

    body: Optional[Union[str, XmlDate]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
