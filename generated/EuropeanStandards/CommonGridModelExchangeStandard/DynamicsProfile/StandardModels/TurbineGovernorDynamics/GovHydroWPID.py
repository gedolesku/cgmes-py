from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovHydroWPID(TurbineGovernorDynamics):
    d: PU = field(metadata={'xpath': 'cim:GovHydroWPID.d'})
    gatmax: PU = field(metadata={'xpath': 'cim:GovHydroWPID.gatmax'})
    gatmin: PU = field(metadata={'xpath': 'cim:GovHydroWPID.gatmin'})
    gv1: PU = field(metadata={'xpath': 'cim:GovHydroWPID.gv1'})
    gv2: PU = field(metadata={'xpath': 'cim:GovHydroWPID.gv2'})
    gv3: PU = field(metadata={'xpath': 'cim:GovHydroWPID.gv3'})
    kd: PU = field(metadata={'xpath': 'cim:GovHydroWPID.kd'})
    ki: PU = field(metadata={'xpath': 'cim:GovHydroWPID.ki'})
    kp: PU = field(metadata={'xpath': 'cim:GovHydroWPID.kp'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovHydroWPID.mwbase'})
    pgv1: PU = field(metadata={'xpath': 'cim:GovHydroWPID.pgv1'})
    pgv2: PU = field(metadata={'xpath': 'cim:GovHydroWPID.pgv2'})
    pgv3: PU = field(metadata={'xpath': 'cim:GovHydroWPID.pgv3'})
    pmax: PU = field(metadata={'xpath': 'cim:GovHydroWPID.pmax'})
    pmin: PU = field(metadata={'xpath': 'cim:GovHydroWPID.pmin'})
    reg: PU = field(metadata={'xpath': 'cim:GovHydroWPID.reg'})
    ta: Seconds = field(metadata={'xpath': 'cim:GovHydroWPID.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:GovHydroWPID.tb'})
    treg: Seconds = field(metadata={'xpath': 'cim:GovHydroWPID.treg'})
    tw: Seconds = field(metadata={'xpath': 'cim:GovHydroWPID.tw'})
    velmax: PU = field(metadata={'xpath': 'cim:GovHydroWPID.velmax'})
    velmin: PU = field(metadata={'xpath': 'cim:GovHydroWPID.velmin'})
