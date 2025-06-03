from dataclasses import dataclass, field

from cgmes24.tag import Tag


@dataclass
class Tags:
    class Meta:
        name = "tags"
        namespace = ""

    tag: list[Tag] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
