from __future__ import annotations
from ...DomainProfile.String import String
from ...StateVariablesProfile.Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field
from typing import Optional, List
# pylint: disable=function-redefined

@dataclass(kw_only=True)
class IdentifiedObject(IdentifiedObject):
    description: Optional[String] = field(default=None, metadata={'xpath': 'cim:IdentifiedObject.description'})
    energyIdentCodeEic: Optional[String] = field(default=None, metadata={'xpath': 'cim:IdentifiedObject.energyIdentCodeEic'})
    mRID: Optional[String] = field(default=None, metadata={'xpath': 'cim:IdentifiedObject.mRID'})
    name: Optional[String] = field(default=None, metadata={'xpath': 'cim:IdentifiedObject.name'})
    shortName: Optional[String] = field(default=None, metadata={'xpath': 'cim:IdentifiedObject.shortName'})
