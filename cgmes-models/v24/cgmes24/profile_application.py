from dataclasses import dataclass, field
from typing import Optional

from cgmes24.applied_profile import AppliedProfile


@dataclass
class ProfileApplication:
    class Meta:
        name = "profileApplication"
        namespace = ""

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
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
    applied_profile: Optional[AppliedProfile] = field(
        default=None,
        metadata={
            "name": "appliedProfile",
            "type": "Element",
            "required": True,
        },
    )
