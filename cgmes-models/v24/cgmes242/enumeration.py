from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sparxsystems.com/profiles/EAUML/1.0"


@dataclass
class Enumeration:
    class Meta:
        name = "enumeration"
        namespace = "http://www.sparxsystems.com/profiles/EAUML/1.0"

    base_enumeration: Optional[str] = field(
        default=None,
        metadata={
            "name": "base_Enumeration",
            "type": "Attribute",
            "required": True,
        },
    )
