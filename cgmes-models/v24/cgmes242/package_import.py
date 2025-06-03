from dataclasses import dataclass, field
from typing import Optional

from cgmes242.imported_package import ImportedPackage


@dataclass
class PackageImport:
    class Meta:
        name = "packageImport"
        namespace = ""

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
            "required": True,
        },
    )
    imported_package: Optional[ImportedPackage] = field(
        default=None,
        metadata={
            "name": "importedPackage",
            "type": "Element",
            "required": True,
        },
    )
