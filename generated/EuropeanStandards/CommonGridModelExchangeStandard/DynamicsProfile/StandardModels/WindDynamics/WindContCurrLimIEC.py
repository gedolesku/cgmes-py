from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ...Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindContCurrLimIEC(IdentifiedObject):
    imax: PU = field(metadata={'xpath': 'cim:WindContCurrLimIEC.imax'})
    imaxdip: PU = field(metadata={'xpath': 'cim:WindContCurrLimIEC.imaxdip'})
    mdfslim: Boolean = field(metadata={'xpath': 'cim:WindContCurrLimIEC.mdfslim'})
    mqpri: Boolean = field(metadata={'xpath': 'cim:WindContCurrLimIEC.mqpri'})
    tufilt: Seconds = field(metadata={'xpath': 'cim:WindContCurrLimIEC.tufilt'})
