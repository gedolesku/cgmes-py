from dataclasses import dataclass, field

from cgmes24.image import Image


@dataclass
class Images:
    class Meta:
        name = "images"
        namespace = ""

    image: list[Image] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
