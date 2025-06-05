from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ...Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindContPType4aIEC(IdentifiedObject):
    dpmax: PU = field(metadata={'xpath': 'cim:WindContPType4aIEC.dpmax'})
    tpord: Seconds = field(metadata={'xpath': 'cim:WindContPType4aIEC.tpord'})
    tufilt: Seconds = field(metadata={'xpath': 'cim:WindContPType4aIEC.tufilt'})
