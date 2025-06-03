from dataclasses import dataclass, field

from cgmes242.connector import Connector


@dataclass
class Connectors:
    class Meta:
        name = "connectors"
        namespace = ""

    connector: list[Connector] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
