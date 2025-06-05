from __future__ import annotations
from ...DomainProfile.String import String
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class IdentifiedObject:
    mRID: Optional[String] = field(default=None, metadata={'xpath': 'cim:IdentifiedObject.mRID'})
    name: Optional[String] = field(default=None, metadata={'xpath': 'cim:IdentifiedObject.name'})
