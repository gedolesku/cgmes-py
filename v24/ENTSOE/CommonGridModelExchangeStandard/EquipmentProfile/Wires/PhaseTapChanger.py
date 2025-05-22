from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.TransformerEnd import TransformerEnd     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.TapChanger import TapChanger

@dataclass
class PhaseTapChanger(TapChanger):
    """A transformer phase shifting tap model that controls the phase angle difference
    across the power transformer and potentially the active power flow through the
    power transformer.  This phase tap model may also impact the voltage magnitude.
    """
    # Phase tap changer associated with this transformer end.
    TransformerEnd_: Optional[TransformerEnd] = None
     