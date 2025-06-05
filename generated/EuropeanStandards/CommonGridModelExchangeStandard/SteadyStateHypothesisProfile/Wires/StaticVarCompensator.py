from __future__ import annotations
from ...DomainProfile.ReactivePower import ReactivePower
from .RegulatingCondEq import RegulatingCondEq
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class StaticVarCompensator(RegulatingCondEq):
    q: ReactivePower = field(metadata={'xpath': 'cim:StaticVarCompensator.q'})
