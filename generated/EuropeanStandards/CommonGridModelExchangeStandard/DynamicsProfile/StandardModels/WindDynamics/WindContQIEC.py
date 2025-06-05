from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ...Core.IdentifiedObject import IdentifiedObject
from .WindLVRTQcontrolModesKind import WindLVRTQcontrolModesKind
from .WindQcontrolModesKind import WindQcontrolModesKind
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindContQIEC(IdentifiedObject):
    iqh1: PU = field(metadata={'xpath': 'cim:WindContQIEC.iqh1'})
    iqmax: PU = field(metadata={'xpath': 'cim:WindContQIEC.iqmax'})
    iqmin: PU = field(metadata={'xpath': 'cim:WindContQIEC.iqmin'})
    iqpost: PU = field(metadata={'xpath': 'cim:WindContQIEC.iqpost'})
    kiq: PU = field(metadata={'xpath': 'cim:WindContQIEC.kiq'})
    kiu: PU = field(metadata={'xpath': 'cim:WindContQIEC.kiu'})
    kpq: PU = field(metadata={'xpath': 'cim:WindContQIEC.kpq'})
    kpu: PU = field(metadata={'xpath': 'cim:WindContQIEC.kpu'})
    kqv: PU = field(metadata={'xpath': 'cim:WindContQIEC.kqv'})
    qmax: PU = field(metadata={'xpath': 'cim:WindContQIEC.qmax'})
    qmin: PU = field(metadata={'xpath': 'cim:WindContQIEC.qmin'})
    rdroop: PU = field(metadata={'xpath': 'cim:WindContQIEC.rdroop'})
    tiq: Seconds = field(metadata={'xpath': 'cim:WindContQIEC.tiq'})
    tpfilt: Seconds = field(metadata={'xpath': 'cim:WindContQIEC.tpfilt'})
    tpost: Seconds = field(metadata={'xpath': 'cim:WindContQIEC.tpost'})
    tqord: Seconds = field(metadata={'xpath': 'cim:WindContQIEC.tqord'})
    tufilt: Seconds = field(metadata={'xpath': 'cim:WindContQIEC.tufilt'})
    udb1: PU = field(metadata={'xpath': 'cim:WindContQIEC.udb1'})
    udb2: PU = field(metadata={'xpath': 'cim:WindContQIEC.udb2'})
    umax: PU = field(metadata={'xpath': 'cim:WindContQIEC.umax'})
    umin: PU = field(metadata={'xpath': 'cim:WindContQIEC.umin'})
    uqdip: PU = field(metadata={'xpath': 'cim:WindContQIEC.uqdip'})
    uref0: PU = field(metadata={'xpath': 'cim:WindContQIEC.uref0'})
    windLVRTQcontrolModesType: WindLVRTQcontrolModesKind = field(metadata={'xpath': 'cim:WindContQIEC.windLVRTQcontrolModesType'})
    windQcontrolModesType: WindQcontrolModesKind = field(metadata={'xpath': 'cim:WindContQIEC.windQcontrolModesType'})
    xdroop: PU = field(metadata={'xpath': 'cim:WindContQIEC.xdroop'})
