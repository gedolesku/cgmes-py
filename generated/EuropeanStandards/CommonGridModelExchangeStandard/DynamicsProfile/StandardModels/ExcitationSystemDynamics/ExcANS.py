from __future__ import annotations
from ....DomainProfile.Integer import Integer
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcANS(ExcitationSystemDynamics):
    blint: Integer = field(metadata={'xpath': 'cim:ExcANS.blint'})
    ifmn: PU = field(metadata={'xpath': 'cim:ExcANS.ifmn'})
    ifmx: PU = field(metadata={'xpath': 'cim:ExcANS.ifmx'})
    k2: Simple_Float = field(metadata={'xpath': 'cim:ExcANS.k2'})
    k3: Simple_Float = field(metadata={'xpath': 'cim:ExcANS.k3'})
    kce: Simple_Float = field(metadata={'xpath': 'cim:ExcANS.kce'})
    krvecc: Integer = field(metadata={'xpath': 'cim:ExcANS.krvecc'})
    kvfif: Integer = field(metadata={'xpath': 'cim:ExcANS.kvfif'})
    t1: Seconds = field(metadata={'xpath': 'cim:ExcANS.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:ExcANS.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:ExcANS.t3'})
    tb: Seconds = field(metadata={'xpath': 'cim:ExcANS.tb'})
    vrmn: PU = field(metadata={'xpath': 'cim:ExcANS.vrmn'})
    vrmx: PU = field(metadata={'xpath': 'cim:ExcANS.vrmx'})
