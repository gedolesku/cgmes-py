from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.Measurement import Measurement

@dataclass
class Analog(Measurement):
    """Analog represents an analog Measurement.
    """
    # If true then this measurement is an active power, reactive power or current
    # with the convention that a positive value measured at the Terminal means power
    # is flowing into the related PowerSystemResource.
    positiveFlowIn_: bool  = None
     