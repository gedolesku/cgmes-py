from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.AccumulatorValue import AccumulatorValue     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.Control import Control

@dataclass
class AccumulatorReset(Control):
    """This command reset the counter value to zero.
    """
    # The accumulator value that is reset by the command.
    AccumulatorValue_ref: Optional[AccumulatorValue] = None
    AccumulatorValue: str = None
     