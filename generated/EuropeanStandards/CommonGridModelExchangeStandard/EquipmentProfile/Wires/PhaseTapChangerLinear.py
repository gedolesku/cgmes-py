from __future__ import annotations
from ...DomainProfile.AngleDegrees import AngleDegrees
from ...DomainProfile.Reactance import Reactance
from .PhaseTapChanger import PhaseTapChanger
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PhaseTapChangerLinear(PhaseTapChanger):
    stepPhaseShiftIncrement: AngleDegrees = field(metadata={'xpath': 'cim:PhaseTapChangerLinear.stepPhaseShiftIncrement'})
    xMax: Reactance = field(metadata={'xpath': 'cim:PhaseTapChangerLinear.xMax'})
    xMin: Reactance = field(metadata={'xpath': 'cim:PhaseTapChangerLinear.xMin'})
