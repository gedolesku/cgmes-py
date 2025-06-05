from __future__ import annotations
from ....DomainProfile.ApparentPower import ApparentPower
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcSK(ExcitationSystemDynamics):
    efdmax: PU = field(metadata={'xpath': 'cim:ExcSK.efdmax'})
    efdmin: PU = field(metadata={'xpath': 'cim:ExcSK.efdmin'})
    emax: PU = field(metadata={'xpath': 'cim:ExcSK.emax'})
    emin: PU = field(metadata={'xpath': 'cim:ExcSK.emin'})
    k: PU = field(metadata={'xpath': 'cim:ExcSK.k'})
    k1: PU = field(metadata={'xpath': 'cim:ExcSK.k1'})
    k2: PU = field(metadata={'xpath': 'cim:ExcSK.k2'})
    kc: PU = field(metadata={'xpath': 'cim:ExcSK.kc'})
    kce: PU = field(metadata={'xpath': 'cim:ExcSK.kce'})
    kd: PU = field(metadata={'xpath': 'cim:ExcSK.kd'})
    kgob: PU = field(metadata={'xpath': 'cim:ExcSK.kgob'})
    kp: PU = field(metadata={'xpath': 'cim:ExcSK.kp'})
    kqi: PU = field(metadata={'xpath': 'cim:ExcSK.kqi'})
    kqob: PU = field(metadata={'xpath': 'cim:ExcSK.kqob'})
    kqp: PU = field(metadata={'xpath': 'cim:ExcSK.kqp'})
    nq: PU = field(metadata={'xpath': 'cim:ExcSK.nq'})
    qconoff: Boolean = field(metadata={'xpath': 'cim:ExcSK.qconoff'})
    qz: PU = field(metadata={'xpath': 'cim:ExcSK.qz'})
    remote: Boolean = field(metadata={'xpath': 'cim:ExcSK.remote'})
    sbase: ApparentPower = field(metadata={'xpath': 'cim:ExcSK.sbase'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcSK.tc'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcSK.te'})
    ti: Seconds = field(metadata={'xpath': 'cim:ExcSK.ti'})
    tp: Seconds = field(metadata={'xpath': 'cim:ExcSK.tp'})
    tr: Seconds = field(metadata={'xpath': 'cim:ExcSK.tr'})
    uimax: PU = field(metadata={'xpath': 'cim:ExcSK.uimax'})
    uimin: PU = field(metadata={'xpath': 'cim:ExcSK.uimin'})
    urmax: PU = field(metadata={'xpath': 'cim:ExcSK.urmax'})
    urmin: PU = field(metadata={'xpath': 'cim:ExcSK.urmin'})
    vtmax: PU = field(metadata={'xpath': 'cim:ExcSK.vtmax'})
    vtmin: PU = field(metadata={'xpath': 'cim:ExcSK.vtmin'})
    yp: PU = field(metadata={'xpath': 'cim:ExcSK.yp'})
