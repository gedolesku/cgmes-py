from __future__ import annotations
from ...DomainProfile.Reactance import Reactance
from .EarthFaultCompensator import EarthFaultCompensator
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GroundingImpedance(EarthFaultCompensator):
    x: Reactance = field(metadata={'xpath': 'cim:GroundingImpedance.x'})
