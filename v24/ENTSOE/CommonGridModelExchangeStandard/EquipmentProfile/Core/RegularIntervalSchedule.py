from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.DateTime import DateTime     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.BasicIntervalSchedule import BasicIntervalSchedule

@dataclass
class RegularIntervalSchedule(BasicIntervalSchedule):
    """The schedule has time points where the time between them is constant.
    """
    # The time between each pair of subsequent regular time points in sequence order.
    timeStep_: Seconds  = None
 
    # The time for the last time point.
    endTime_: DateTime  = None
     