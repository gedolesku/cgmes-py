from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PerCent import PerCent     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Reactance import Reactance     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.PhaseTapChanger import PhaseTapChanger

@dataclass
class PhaseTapChangerNonLinear(PhaseTapChanger):
    """The non-linear phase tap changer describes the non-linear behavior of a phase
    tap changer. This is a base class for the symmetrical and asymmetrical phase
    tap changer models. The details of these models can be found in the IEC 61970-
    301 document.
    """
    # The voltage step increment on the out of phase winding specified in percent of
    # nominal voltage of the transformer end.
    voltageStepIncrement_: PerCent  = None
 
    # The reactance depend on the tap position according to a "u" shaped curve. The
    # maximum reactance (xMax) appear at the low and high tap positions.
    xMax_: Reactance  = None
 
    # The reactance depend on the tap position according to a "u" shaped curve. The
    # minimum reactance (xMin) appear at the mid tap position.
    xMin_: Reactance  = None
     