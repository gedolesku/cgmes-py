from dataclasses import dataclass, field
from typing import Optional

from cgmes242.packaged_element import PackagedElement
from cgmes242.profile_application import ProfileApplication

__NAMESPACE__ = "http://www.omg.org/spec/UML/20090901"


@dataclass
class Model1:
    class Meta:
        name = "Model"
        namespace = "http://www.omg.org/spec/UML/20090901"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
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
    packaged_element: Optional[PackagedElement] = field(
        default=None,
        metadata={
            "name": "packagedElement",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    profile_application: list[ProfileApplication] = field(
        default_factory=list,
        metadata={
            "name": "profileApplication",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
