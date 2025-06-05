from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcELIN2(ExcitationSystemDynamics):
    efdbas: PU = field(metadata={'xpath': 'cim:ExcELIN2.efdbas'})
    iefmax: PU = field(metadata={'xpath': 'cim:ExcELIN2.iefmax'})
    iefmax2: PU = field(metadata={'xpath': 'cim:ExcELIN2.iefmax2'})
    iefmin: PU = field(metadata={'xpath': 'cim:ExcELIN2.iefmin'})
    k1: PU = field(metadata={'xpath': 'cim:ExcELIN2.k1'})
    k1ec: PU = field(metadata={'xpath': 'cim:ExcELIN2.k1ec'})
    k2: PU = field(metadata={'xpath': 'cim:ExcELIN2.k2'})
    k3: PU = field(metadata={'xpath': 'cim:ExcELIN2.k3'})
    k4: PU = field(metadata={'xpath': 'cim:ExcELIN2.k4'})
    kd1: PU = field(metadata={'xpath': 'cim:ExcELIN2.kd1'})
    ke2: PU = field(metadata={'xpath': 'cim:ExcELIN2.ke2'})
    ketb: PU = field(metadata={'xpath': 'cim:ExcELIN2.ketb'})
    pid1max: PU = field(metadata={'xpath': 'cim:ExcELIN2.pid1max'})
    seve1: PU = field(metadata={'xpath': 'cim:ExcELIN2.seve1'})
    seve2: PU = field(metadata={'xpath': 'cim:ExcELIN2.seve2'})
    tb1: Seconds = field(metadata={'xpath': 'cim:ExcELIN2.tb1'})
    te: Seconds = field(metadata={'xpath': 'cim:ExcELIN2.te'})
    te2: Seconds = field(metadata={'xpath': 'cim:ExcELIN2.te2'})
    ti1: PU = field(metadata={'xpath': 'cim:ExcELIN2.ti1'})
    ti3: Seconds = field(metadata={'xpath': 'cim:ExcELIN2.ti3'})
    ti4: Seconds = field(metadata={'xpath': 'cim:ExcELIN2.ti4'})
    tr4: Seconds = field(metadata={'xpath': 'cim:ExcELIN2.tr4'})
    upmax: PU = field(metadata={'xpath': 'cim:ExcELIN2.upmax'})
    upmin: PU = field(metadata={'xpath': 'cim:ExcELIN2.upmin'})
    ve1: PU = field(metadata={'xpath': 'cim:ExcELIN2.ve1'})
    ve2: PU = field(metadata={'xpath': 'cim:ExcELIN2.ve2'})
    xp: PU = field(metadata={'xpath': 'cim:ExcELIN2.xp'})
