from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcELIN1(ExcitationSystemDynamics):
    dpnf: PU = field(metadata={'xpath': 'cim:ExcELIN1.dpnf'})
    efmax: PU = field(metadata={'xpath': 'cim:ExcELIN1.efmax'})
    efmin: PU = field(metadata={'xpath': 'cim:ExcELIN1.efmin'})
    ks1: PU = field(metadata={'xpath': 'cim:ExcELIN1.ks1'})
    ks2: PU = field(metadata={'xpath': 'cim:ExcELIN1.ks2'})
    smax: PU = field(metadata={'xpath': 'cim:ExcELIN1.smax'})
    tfi: Seconds = field(metadata={'xpath': 'cim:ExcELIN1.tfi'})
    tnu: Seconds = field(metadata={'xpath': 'cim:ExcELIN1.tnu'})
    ts1: Seconds = field(metadata={'xpath': 'cim:ExcELIN1.ts1'})
    ts2: Seconds = field(metadata={'xpath': 'cim:ExcELIN1.ts2'})
    tsw: Seconds = field(metadata={'xpath': 'cim:ExcELIN1.tsw'})
    vpi: PU = field(metadata={'xpath': 'cim:ExcELIN1.vpi'})
    vpnf: PU = field(metadata={'xpath': 'cim:ExcELIN1.vpnf'})
    vpu: PU = field(metadata={'xpath': 'cim:ExcELIN1.vpu'})
    xe: PU = field(metadata={'xpath': 'cim:ExcELIN1.xe'})
