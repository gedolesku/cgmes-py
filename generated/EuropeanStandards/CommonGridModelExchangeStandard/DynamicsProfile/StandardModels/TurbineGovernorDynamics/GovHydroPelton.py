from __future__ import annotations
from ....DomainProfile.Area import Area
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.Frequency import Frequency
from ....DomainProfile.Length import Length
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from ....DomainProfile.VolumeFlowRate import VolumeFlowRate
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovHydroPelton(TurbineGovernorDynamics):
    av0: Area = field(metadata={'xpath': 'cim:GovHydroPelton.av0'})
    av1: Area = field(metadata={'xpath': 'cim:GovHydroPelton.av1'})
    bp: PU = field(metadata={'xpath': 'cim:GovHydroPelton.bp'})
    db1: Frequency = field(metadata={'xpath': 'cim:GovHydroPelton.db1'})
    db2: Frequency = field(metadata={'xpath': 'cim:GovHydroPelton.db2'})
    h1: Length = field(metadata={'xpath': 'cim:GovHydroPelton.h1'})
    h2: Length = field(metadata={'xpath': 'cim:GovHydroPelton.h2'})
    hn: Length = field(metadata={'xpath': 'cim:GovHydroPelton.hn'})
    kc: PU = field(metadata={'xpath': 'cim:GovHydroPelton.kc'})
    kg: PU = field(metadata={'xpath': 'cim:GovHydroPelton.kg'})
    qc0: PU = field(metadata={'xpath': 'cim:GovHydroPelton.qc0'})
    qn: VolumeFlowRate = field(metadata={'xpath': 'cim:GovHydroPelton.qn'})
    simplifiedPelton: Boolean = field(metadata={'xpath': 'cim:GovHydroPelton.simplifiedPelton'})
    staticCompensating: Boolean = field(metadata={'xpath': 'cim:GovHydroPelton.staticCompensating'})
    ta: Seconds = field(metadata={'xpath': 'cim:GovHydroPelton.ta'})
    ts: Seconds = field(metadata={'xpath': 'cim:GovHydroPelton.ts'})
    tv: Seconds = field(metadata={'xpath': 'cim:GovHydroPelton.tv'})
    twnc: Seconds = field(metadata={'xpath': 'cim:GovHydroPelton.twnc'})
    twng: Seconds = field(metadata={'xpath': 'cim:GovHydroPelton.twng'})
    tx: Seconds = field(metadata={'xpath': 'cim:GovHydroPelton.tx'})
    va: Simple_Float = field(metadata={'xpath': 'cim:GovHydroPelton.va'})
    valvmax: PU = field(metadata={'xpath': 'cim:GovHydroPelton.valvmax'})
    valvmin: PU = field(metadata={'xpath': 'cim:GovHydroPelton.valvmin'})
    vav: PU = field(metadata={'xpath': 'cim:GovHydroPelton.vav'})
    vc: Simple_Float = field(metadata={'xpath': 'cim:GovHydroPelton.vc'})
    vcv: PU = field(metadata={'xpath': 'cim:GovHydroPelton.vcv'})
    waterTunnelSurgeChamberSimulation: Boolean = field(metadata={'xpath': 'cim:GovHydroPelton.waterTunnelSurgeChamberSimulation'})
    zsfc: Length = field(metadata={'xpath': 'cim:GovHydroPelton.zsfc'})
