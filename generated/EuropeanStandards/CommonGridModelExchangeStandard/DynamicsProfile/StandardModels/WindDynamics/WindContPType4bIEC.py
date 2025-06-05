from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ...Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindContPType4bIEC(IdentifiedObject):
    dpmax: PU = field(metadata={'xpath': 'cim:WindContPType4bIEC.dpmax'})
    tpaero: Seconds = field(metadata={'xpath': 'cim:WindContPType4bIEC.tpaero'})
    tpord: Seconds = field(metadata={'xpath': 'cim:WindContPType4bIEC.tpord'})
    tufilt: Seconds = field(metadata={'xpath': 'cim:WindContPType4bIEC.tufilt'})
