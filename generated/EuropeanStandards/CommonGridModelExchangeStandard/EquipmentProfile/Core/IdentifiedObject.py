from __future__ import annotations
from ...DomainProfile.String import String
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class IdentifiedObject:
    name: String = field(metadata={'xpath': 'cim:IdentifiedObject.name'})
    description: Optional[String] = field(default=None, metadata={'xpath': 'cim:IdentifiedObject.description'})
    energyIdentCodeEic: Optional[String] = field(default=None, metadata={'xpath': 'cim:IdentifiedObject.energyIdentCodeEic'})
    mRID: Optional[String] = field(default=None, metadata={'xpath': 'cim:IdentifiedObject.mRID'})
    shortName: Optional[String] = field(default=None, metadata={'xpath': 'cim:IdentifiedObject.shortName'})
