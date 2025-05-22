from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.AngleDegrees import AngleDegrees     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Reactance import Reactance     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.PhaseTapChanger import PhaseTapChanger

@dataclass
class PhaseTapChangerLinear(PhaseTapChanger):
    """Describes a tap changer with a linear relation between the tap step and the
    phase angle difference across the transformer. This is a mathematical model
    that is an approximation of a real phase tap changer.
      The phase angle is computed as stepPhaseShitfIncrement times the tap position.
    
      The secondary side voltage magnitude is the same as at the primary side.
    """
    # Phase shift per step position. A positive value indicates a positive phase
    # shift from the winding where the tap is located to the other winding (for a two-
    # winding transformer).
    # The actual phase shift increment might be more accurately computed from the
    # symmetrical or asymmetrical models or a tap step table lookup if those are
    # available.
    stepPhaseShiftIncrement_: AngleDegrees  = None
 
    # The reactance depend on the tap position according to a "u" shaped curve. The
    # maximum reactance (xMax) appear at the low and high tap positions.
    xMax_: Reactance  = None
 
    # The reactance depend on the tap position according to a "u" shaped curve. The
    # minimum reactance (xMin) appear at the mid tap position.
    xMin_: Reactance  = None
     