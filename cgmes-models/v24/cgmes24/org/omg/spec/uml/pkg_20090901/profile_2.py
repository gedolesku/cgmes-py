from dataclasses import dataclass, field
from typing import Optional

from cgmes24.owned_comment import OwnedComment
from cgmes24.package_import import PackageImport
from cgmes24.packaged_element import PackagedElement

__NAMESPACE__ = "http://www.omg.org/spec/UML/20090901"


@dataclass
class Profile2:
    class Meta:
        name = "Profile"
        namespace = "http://www.omg.org/spec/UML/20090901"

    version: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
            "required": True,
        },
    )
    ns_prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "nsPrefix",
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    metamodel_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "metamodelReference",
            "type": "Attribute",
            "required": True,
        },
    )
    owned_comment: Optional[OwnedComment] = field(
        default=None,
        metadata={
            "name": "ownedComment",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    package_import: Optional[PackageImport] = field(
        default=None,
        metadata={
            "name": "packageImport",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    packaged_element: list[PackagedElement] = field(
        default_factory=list,
        metadata={
            "name": "packagedElement",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
