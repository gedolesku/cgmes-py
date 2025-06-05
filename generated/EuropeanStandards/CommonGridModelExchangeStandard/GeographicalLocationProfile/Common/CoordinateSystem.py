from __future__ import annotations
from ...DomainProfile.String import String
from ..Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class CoordinateSystem(IdentifiedObject):
    crsUrn: String = field(metadata={'xpath': 'cim:CoordinateSystem.crsUrn'})
