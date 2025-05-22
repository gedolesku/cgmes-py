from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.TransformerControlMode import TransformerControlMode     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PerCent import PerCent     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.RatioTapChangerTable import RatioTapChangerTable     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.TransformerEnd import TransformerEnd     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.TapChanger import TapChanger

@dataclass
class RatioTapChanger(TapChanger):
    """A tap changer that changes the voltage ratio impacting the voltage magnitude
    but not the phase angle across the transformer.
    """
    # Specifies the regulation control mode (voltage or reactive) of the
    # RatioTapChanger.
    tculControlMode_: TransformerControlMode  = None
 
    # Tap step increment, in per cent of nominal voltage, per step position.
    stepVoltageIncrement_: PerCent  = None
 
    # The ratio tap changer of this tap ratio table.
    RatioTapChangerTable_: Optional[RatioTapChangerTable] = None
 
    # Ratio tap changer associated with this transformer end.
    TransformerEnd_: Optional[TransformerEnd] = None
     