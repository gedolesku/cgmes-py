from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from ...Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindContPType3IEC(IdentifiedObject):
    dpmax: PU = field(metadata={'xpath': 'cim:WindContPType3IEC.dpmax'})
    dtrisemaxlvrt: PU = field(metadata={'xpath': 'cim:WindContPType3IEC.dtrisemaxlvrt'})
    kdtd: PU = field(metadata={'xpath': 'cim:WindContPType3IEC.kdtd'})
    kip: PU = field(metadata={'xpath': 'cim:WindContPType3IEC.kip'})
    kpp: PU = field(metadata={'xpath': 'cim:WindContPType3IEC.kpp'})
    mplvrt: Boolean = field(metadata={'xpath': 'cim:WindContPType3IEC.mplvrt'})
    omegaoffset: PU = field(metadata={'xpath': 'cim:WindContPType3IEC.omegaoffset'})
    pdtdmax: PU = field(metadata={'xpath': 'cim:WindContPType3IEC.pdtdmax'})
    rramp: PU = field(metadata={'xpath': 'cim:WindContPType3IEC.rramp'})
    tdvs: Seconds = field(metadata={'xpath': 'cim:WindContPType3IEC.tdvs'})
    temin: PU = field(metadata={'xpath': 'cim:WindContPType3IEC.temin'})
    tomegafilt: Seconds = field(metadata={'xpath': 'cim:WindContPType3IEC.tomegafilt'})
    tpfilt: Seconds = field(metadata={'xpath': 'cim:WindContPType3IEC.tpfilt'})
    tpord: PU = field(metadata={'xpath': 'cim:WindContPType3IEC.tpord'})
    tufilt: Seconds = field(metadata={'xpath': 'cim:WindContPType3IEC.tufilt'})
    tuscale: PU = field(metadata={'xpath': 'cim:WindContPType3IEC.tuscale'})
    twref: Seconds = field(metadata={'xpath': 'cim:WindContPType3IEC.twref'})
    udvs: PU = field(metadata={'xpath': 'cim:WindContPType3IEC.udvs'})
    updip: PU = field(metadata={'xpath': 'cim:WindContPType3IEC.updip'})
    wdtd: PU = field(metadata={'xpath': 'cim:WindContPType3IEC.wdtd'})
    zeta: Simple_Float = field(metadata={'xpath': 'cim:WindContPType3IEC.zeta'})
