from dataclasses import dataclass, field

from cgmes24.org.omg.spec.uml.pkg_20090901.profile_2 import Profile2


@dataclass
class Profiles:
    class Meta:
        name = "profiles"
        namespace = ""

    profile: list[Profile2] = field(
        default_factory=list,
        metadata={
            "name": "Profile",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/UML/20090901",
            "min_occurs": 1,
        },
    )
