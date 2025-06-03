from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ImportedPackage:
    class Meta:
        name = "importedPackage"
        namespace = ""

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
