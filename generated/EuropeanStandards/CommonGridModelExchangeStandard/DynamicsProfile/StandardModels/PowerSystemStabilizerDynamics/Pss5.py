from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Pss5(PowerSystemStabilizerDynamics):
    ctw2: Boolean = field(metadata={'xpath': 'cim:Pss5.ctw2'})
    deadband: PU = field(metadata={'xpath': 'cim:Pss5.deadband'})
    isfreq: Boolean = field(metadata={'xpath': 'cim:Pss5.isfreq'})
    kf: Simple_Float = field(metadata={'xpath': 'cim:Pss5.kf'})
    kpe: Simple_Float = field(metadata={'xpath': 'cim:Pss5.kpe'})
    kpss: Simple_Float = field(metadata={'xpath': 'cim:Pss5.kpss'})
    pmm: PU = field(metadata={'xpath': 'cim:Pss5.pmm'})
    tl1: Seconds = field(metadata={'xpath': 'cim:Pss5.tl1'})
    tl2: Seconds = field(metadata={'xpath': 'cim:Pss5.tl2'})
    tl3: Seconds = field(metadata={'xpath': 'cim:Pss5.tl3'})
    tl4: Seconds = field(metadata={'xpath': 'cim:Pss5.tl4'})
    tpe: Seconds = field(metadata={'xpath': 'cim:Pss5.tpe'})
    tw1: Seconds = field(metadata={'xpath': 'cim:Pss5.tw1'})
    tw2: Seconds = field(metadata={'xpath': 'cim:Pss5.tw2'})
    vadat: Boolean = field(metadata={'xpath': 'cim:Pss5.vadat'})
    vsmn: PU = field(metadata={'xpath': 'cim:Pss5.vsmn'})
    vsmx: PU = field(metadata={'xpath': 'cim:Pss5.vsmx'})
