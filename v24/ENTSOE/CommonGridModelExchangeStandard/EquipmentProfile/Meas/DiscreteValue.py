from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.MeasurementValue import MeasurementValue
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.Discrete import Discrete     

@dataclass
class DiscreteValue(MeasurementValue):
    """DiscreteValue represents a discrete MeasurementValue.
    """
    # The value to supervise.
    value_: int  = None
 
    # The values connected to this measurement.
    Discrete_: Optional[Discrete] = None
     