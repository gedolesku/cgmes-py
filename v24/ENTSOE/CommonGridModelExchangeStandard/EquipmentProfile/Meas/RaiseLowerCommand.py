from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.ValueAliasSet import ValueAliasSet     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.AnalogControl import AnalogControl

@dataclass
class RaiseLowerCommand(AnalogControl):
    """An analog control that increase or decrease a set point value with pulses.
    """
    # The ValueAliasSet used for translation of a Control value to a name.
    ValueAliasSet_ref: Optional[ValueAliasSet] = None
    ValueAliasSet: str = None
     