from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.PhaseTapChanger import PhaseTapChanger

@dataclass
class PhaseTapChangerLinear(PhaseTapChanger):
    """Describes a tap changer with a linear relation between the tap step and the
    phase angle difference across the transformer. This is a mathematical model
    that is an approximation of a real phase tap changer.
      The phase angle is computed as stepPhaseShitfIncrement times the tap position.
    
      The secondary side voltage magnitude is the same as at the primary side.
    """
    pass
