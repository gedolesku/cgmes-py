from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.Reactance import Reactance
from ...DomainProfile.ReactivePower import ReactivePower
from ...DomainProfile.Resistance import Resistance
from ..Wires.ReactiveCapabilityCurve import ReactiveCapabilityCurve
from .EquivalentEquipment import EquivalentEquipment
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class EquivalentInjection(EquivalentEquipment):
    r: Resistance = field(metadata={'xpath': 'cim:EquivalentInjection.r'})
    r0: Resistance = field(metadata={'xpath': 'cim:EquivalentInjection.r0'})
    r2: Resistance = field(metadata={'xpath': 'cim:EquivalentInjection.r2'})
    regulationCapability: Boolean = field(metadata={'xpath': 'cim:EquivalentInjection.regulationCapability'})
    x: Reactance = field(metadata={'xpath': 'cim:EquivalentInjection.x'})
    x0: Reactance = field(metadata={'xpath': 'cim:EquivalentInjection.x0'})
    x2: Reactance = field(metadata={'xpath': 'cim:EquivalentInjection.x2'})
    maxP: Optional[ActivePower] = field(default=None, metadata={'xpath': 'cim:EquivalentInjection.maxP'})
    maxQ: Optional[ReactivePower] = field(default=None, metadata={'xpath': 'cim:EquivalentInjection.maxQ'})
    minP: Optional[ActivePower] = field(default=None, metadata={'xpath': 'cim:EquivalentInjection.minP'})
    minQ: Optional[ReactivePower] = field(default=None, metadata={'xpath': 'cim:EquivalentInjection.minQ'})
    ReactiveCapabilityCurve_id: str | None = field(default=None, metadata={"xpath": "cim:EquivalentInjection.ReactiveCapabilityCurve/@rdf:resource", "pattern": r"^#.+$"})
    ReactiveCapabilityCurve_ref: ReactiveCapabilityCurve | None = None
