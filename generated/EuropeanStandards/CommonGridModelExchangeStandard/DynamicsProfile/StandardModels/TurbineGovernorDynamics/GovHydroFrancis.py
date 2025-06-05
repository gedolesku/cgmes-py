from __future__ import annotations
from ....DomainProfile.Area import Area
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.Frequency import Frequency
from ....DomainProfile.Length import Length
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from ....DomainProfile.VolumeFlowRate import VolumeFlowRate
from .FrancisGovernorControlKind import FrancisGovernorControlKind
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovHydroFrancis(TurbineGovernorDynamics):
    am: PU = field(metadata={'xpath': 'cim:GovHydroFrancis.am'})
    av0: Area = field(metadata={'xpath': 'cim:GovHydroFrancis.av0'})
    av1: Area = field(metadata={'xpath': 'cim:GovHydroFrancis.av1'})
    bp: PU = field(metadata={'xpath': 'cim:GovHydroFrancis.bp'})
    db1: Frequency = field(metadata={'xpath': 'cim:GovHydroFrancis.db1'})
    etamax: PU = field(metadata={'xpath': 'cim:GovHydroFrancis.etamax'})
    governorControl: FrancisGovernorControlKind = field(metadata={'xpath': 'cim:GovHydroFrancis.governorControl'})
    h1: Length = field(metadata={'xpath': 'cim:GovHydroFrancis.h1'})
    h2: Length = field(metadata={'xpath': 'cim:GovHydroFrancis.h2'})
    hn: Length = field(metadata={'xpath': 'cim:GovHydroFrancis.hn'})
    kc: PU = field(metadata={'xpath': 'cim:GovHydroFrancis.kc'})
    kg: PU = field(metadata={'xpath': 'cim:GovHydroFrancis.kg'})
    kt: PU = field(metadata={'xpath': 'cim:GovHydroFrancis.kt'})
    qc0: PU = field(metadata={'xpath': 'cim:GovHydroFrancis.qc0'})
    qn: VolumeFlowRate = field(metadata={'xpath': 'cim:GovHydroFrancis.qn'})
    ta: Seconds = field(metadata={'xpath': 'cim:GovHydroFrancis.ta'})
    td: Seconds = field(metadata={'xpath': 'cim:GovHydroFrancis.td'})
    ts: Seconds = field(metadata={'xpath': 'cim:GovHydroFrancis.ts'})
    twnc: Seconds = field(metadata={'xpath': 'cim:GovHydroFrancis.twnc'})
    twng: Seconds = field(metadata={'xpath': 'cim:GovHydroFrancis.twng'})
    tx: Seconds = field(metadata={'xpath': 'cim:GovHydroFrancis.tx'})
    va: Simple_Float = field(metadata={'xpath': 'cim:GovHydroFrancis.va'})
    valvmax: PU = field(metadata={'xpath': 'cim:GovHydroFrancis.valvmax'})
    valvmin: PU = field(metadata={'xpath': 'cim:GovHydroFrancis.valvmin'})
    vc: Simple_Float = field(metadata={'xpath': 'cim:GovHydroFrancis.vc'})
    waterTunnelSurgeChamberSimulation: Boolean = field(metadata={'xpath': 'cim:GovHydroFrancis.waterTunnelSurgeChamberSimulation'})
    zsfc: Length = field(metadata={'xpath': 'cim:GovHydroFrancis.zsfc'})
