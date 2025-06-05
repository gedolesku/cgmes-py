from __future__ import annotations
from ....DomainProfile.AngleDegrees import AngleDegrees
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcST3A(ExcitationSystemDynamics):
    efdmax: PU = field(metadata={'xpath': 'cim:ExcST3A.efdmax'})
    kc: PU = field(metadata={'xpath': 'cim:ExcST3A.kc'})
    kg: PU = field(metadata={'xpath': 'cim:ExcST3A.kg'})
    ki: PU = field(metadata={'xpath': 'cim:ExcST3A.ki'})
    kj: PU = field(metadata={'xpath': 'cim:ExcST3A.kj'})
    km: PU = field(metadata={'xpath': 'cim:ExcST3A.km'})
    kp: PU = field(metadata={'xpath': 'cim:ExcST3A.kp'})
    ks: PU = field(metadata={'xpath': 'cim:ExcST3A.ks'})
    ks1: PU = field(metadata={'xpath': 'cim:ExcST3A.ks1'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcST3A.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:ExcST3A.tc'})
    thetap: AngleDegrees = field(metadata={'xpath': 'cim:ExcST3A.thetap'})
    tm: Seconds = field(metadata={'xpath': 'cim:ExcST3A.tm'})
    vbmax: PU = field(metadata={'xpath': 'cim:ExcST3A.vbmax'})
    vgmax: PU = field(metadata={'xpath': 'cim:ExcST3A.vgmax'})
    vimax: PU = field(metadata={'xpath': 'cim:ExcST3A.vimax'})
    vimin: PU = field(metadata={'xpath': 'cim:ExcST3A.vimin'})
    vrmax: PU = field(metadata={'xpath': 'cim:ExcST3A.vrmax'})
    vrmin: PU = field(metadata={'xpath': 'cim:ExcST3A.vrmin'})
    xl: PU = field(metadata={'xpath': 'cim:ExcST3A.xl'})
