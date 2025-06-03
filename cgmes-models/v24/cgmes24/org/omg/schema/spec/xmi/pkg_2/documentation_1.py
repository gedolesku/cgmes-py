from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://schema.omg.org/spec/XMI/2.1"


@dataclass
class Documentation1:
    class Meta:
        name = "Documentation"
        namespace = "http://schema.omg.org/spec/XMI/2.1"

    exporter: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    exporter_version: Optional[float] = field(
        default=None,
        metadata={
            "name": "exporterVersion",
            "type": "Attribute",
            "required": True,
        },
    )
