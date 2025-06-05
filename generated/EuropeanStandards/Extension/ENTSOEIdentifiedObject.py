from __future__ import annotations
from ..CommonGridModelExchangeStandard.DomainProfile.String import String
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class ENTSOEIdentifiedObject:
    energyIdentCodeEic: Optional[String] = field(default=None, metadata={'xpath': 'cim:ENTSOEIdentifiedObject.energyIdentCodeEic'})
    shortName: Optional[String] = field(default=None, metadata={'xpath': 'cim:ENTSOEIdentifiedObject.shortName'})
