from dataclasses import dataclass, field
from typing import Optional

from cgmes24.packaged_element import PackagedElement


@dataclass
class Primitivetypes:
    class Meta:
        name = "primitivetypes"
        namespace = ""

    packaged_element: Optional[PackagedElement] = field(
        default=None,
        metadata={
            "name": "packagedElement",
            "type": "Element",
            "required": True,
        },
    )
