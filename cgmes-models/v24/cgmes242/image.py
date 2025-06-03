from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Image:
    class Meta:
        name = "image"
        namespace = ""

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    image_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "imageID",
            "type": "Attribute",
            "required": True,
        },
    )
    dt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:schemas-microsoft-com:datatypes",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
