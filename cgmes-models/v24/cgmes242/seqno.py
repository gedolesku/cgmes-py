from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"


@dataclass
class Seqno:
    class Meta:
        name = "seqno"
        namespace = "http://www.sparxsystems.com/profiles/thecustomprofile/1.0"

    base_association: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Association",
            "type": "Attribute",
            "required": True,
        },
    )
    seqno: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
