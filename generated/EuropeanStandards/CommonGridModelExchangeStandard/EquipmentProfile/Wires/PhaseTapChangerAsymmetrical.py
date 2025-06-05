from __future__ import annotations
from ...DomainProfile.AngleDegrees import AngleDegrees
from .PhaseTapChangerNonLinear import PhaseTapChangerNonLinear
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PhaseTapChangerAsymmetrical(PhaseTapChangerNonLinear):
    windingConnectionAngle: AngleDegrees = field(metadata={'xpath': 'cim:PhaseTapChangerAsymmetrical.windingConnectionAngle'})
