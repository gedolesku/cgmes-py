from __future__ import annotations
from ...DomainProfile.String import String
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class IdentifiedObject:
    description: String = field(metadata={'xpath': 'cim:IdentifiedObject.description'})
    name: String = field(metadata={'xpath': 'cim:IdentifiedObject.name'})
    shortName: String = field(metadata={'xpath': 'cim:IdentifiedObject.shortName'})
    energyIdentCodeEic: Optional[String] = field(default=None, metadata={'xpath': 'cim:IdentifiedObject.energyIdentCodeEic'})
    mRID: Optional[String] = field(default=None, metadata={'xpath': 'cim:IdentifiedObject.mRID'})
