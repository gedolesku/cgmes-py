from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovHydroIEEE0(TurbineGovernorDynamics):
    k: PU = field(metadata={'xpath': 'cim:GovHydroIEEE0.k'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovHydroIEEE0.mwbase'})
    pmax: PU = field(metadata={'xpath': 'cim:GovHydroIEEE0.pmax'})
    pmin: PU = field(metadata={'xpath': 'cim:GovHydroIEEE0.pmin'})
    t1: Seconds = field(metadata={'xpath': 'cim:GovHydroIEEE0.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:GovHydroIEEE0.t2'})
    t3: Seconds = field(metadata={'xpath': 'cim:GovHydroIEEE0.t3'})
    t4: Seconds = field(metadata={'xpath': 'cim:GovHydroIEEE0.t4'})
