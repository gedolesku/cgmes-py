from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Pss1(PowerSystemStabilizerDynamics):
    kf: Simple_Float = field(metadata={'xpath': 'cim:Pss1.kf'})
    kpe: Simple_Float = field(metadata={'xpath': 'cim:Pss1.kpe'})
    ks: Simple_Float = field(metadata={'xpath': 'cim:Pss1.ks'})
    kw: Simple_Float = field(metadata={'xpath': 'cim:Pss1.kw'})
    pmin: PU = field(metadata={'xpath': 'cim:Pss1.pmin'})
    t10: Seconds = field(metadata={'xpath': 'cim:Pss1.t10'})
    t5: Seconds = field(metadata={'xpath': 'cim:Pss1.t5'})
    t6: Seconds = field(metadata={'xpath': 'cim:Pss1.t6'})
    t7: Seconds = field(metadata={'xpath': 'cim:Pss1.t7'})
    t8: Seconds = field(metadata={'xpath': 'cim:Pss1.t8'})
    t9: Seconds = field(metadata={'xpath': 'cim:Pss1.t9'})
    tpe: Seconds = field(metadata={'xpath': 'cim:Pss1.tpe'})
    vadat: Boolean = field(metadata={'xpath': 'cim:Pss1.vadat'})
    vsmn: PU = field(metadata={'xpath': 'cim:Pss1.vsmn'})
    vsmx: PU = field(metadata={'xpath': 'cim:Pss1.vsmx'})
