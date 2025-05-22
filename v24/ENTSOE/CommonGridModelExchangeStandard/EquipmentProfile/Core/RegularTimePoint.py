from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.RegularIntervalSchedule import RegularIntervalSchedule     

@dataclass
class RegularTimePoint:
    """Time point for a schedule where the time between the consecutive points is
    constant.
    """
    # The position of the regular time point in the sequence. Note that time points
    # don't have to be sequential, i.e. time points may be omitted. The actual time
    # for a RegularTimePoint is computed by multiplying the associated regular
    # interval schedule's time step with the regular time point sequence number and
    # adding the associated schedules start time.
    sequenceNumber_: int  = None
 
    # The first value at the time. The meaning of the value is defined by the derived
    # type of the associated schedule.
    value1_: Simple_Float  = None
 
    # The second value at the time. The meaning of the value is defined by the
    # derived type of the associated schedule.
    value2_: Simple_Float  = None
 
    # Regular interval schedule containing this time point.
    RegularIntervalSchedule_: Optional[RegularIntervalSchedule] = None
     