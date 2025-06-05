from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.CurrentFlow import CurrentFlow
from ...DomainProfile.PU import PU
from ...DomainProfile.PerCent import PerCent
from ...DomainProfile.Reactance import Reactance
from ...DomainProfile.ReactivePower import ReactivePower
from ...DomainProfile.Resistance import Resistance
from ...DomainProfile.Simple_Float import Simple_Float
from .ReactiveCapabilityCurve import ReactiveCapabilityCurve
from .RotatingMachine import RotatingMachine
from .ShortCircuitRotorKind import ShortCircuitRotorKind
from .SynchronousMachineKind import SynchronousMachineKind
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class SynchronousMachine(RotatingMachine):
    earthing: Boolean = field(metadata={'xpath': 'cim:SynchronousMachine.earthing'})
    r: Resistance = field(metadata={'xpath': 'cim:SynchronousMachine.r'})
    r0: PU = field(metadata={'xpath': 'cim:SynchronousMachine.r0'})
    r2: PU = field(metadata={'xpath': 'cim:SynchronousMachine.r2'})
    satDirectSubtransX: PU = field(metadata={'xpath': 'cim:SynchronousMachine.satDirectSubtransX'})
    type: SynchronousMachineKind = field(metadata={'xpath': 'cim:SynchronousMachine.type'})
    x0: PU = field(metadata={'xpath': 'cim:SynchronousMachine.x0'})
    x2: PU = field(metadata={'xpath': 'cim:SynchronousMachine.x2'})
    earthingStarPointR: Optional[Resistance] = field(default=None, metadata={'xpath': 'cim:SynchronousMachine.earthingStarPointR'})
    earthingStarPointX: Optional[Reactance] = field(default=None, metadata={'xpath': 'cim:SynchronousMachine.earthingStarPointX'})
    ikk: Optional[CurrentFlow] = field(default=None, metadata={'xpath': 'cim:SynchronousMachine.ikk'})
    maxQ: Optional[ReactivePower] = field(default=None, metadata={'xpath': 'cim:SynchronousMachine.maxQ'})
    minQ: Optional[ReactivePower] = field(default=None, metadata={'xpath': 'cim:SynchronousMachine.minQ'})
    mu: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:SynchronousMachine.mu'})
    qPercent: Optional[PerCent] = field(default=None, metadata={'xpath': 'cim:SynchronousMachine.qPercent'})
    satDirectSyncX: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachine.satDirectSyncX'})
    satDirectTransX: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachine.satDirectTransX'})
    shortCircuitRotorType: Optional[ShortCircuitRotorKind] = field(default=None, metadata={'xpath': 'cim:SynchronousMachine.shortCircuitRotorType'})
    voltageRegulationRange: Optional[PerCent] = field(default=None, metadata={'xpath': 'cim:SynchronousMachine.voltageRegulationRange'})
    InitialReactiveCapabilityCurve_id: str | None = field(default=None, metadata={"xpath": "cim:SynchronousMachine.InitialReactiveCapabilityCurve/@rdf:resource", "pattern": r"^#.+$"})
    InitialReactiveCapabilityCurve_ref: ReactiveCapabilityCurve | None = None
