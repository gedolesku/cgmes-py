from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MemberEnd:
    class Meta:
        name = "memberEnd"
        namespace = ""

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
            "required": True,
        },
    )
