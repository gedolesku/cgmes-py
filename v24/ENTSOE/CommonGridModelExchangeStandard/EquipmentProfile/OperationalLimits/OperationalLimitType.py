from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.OperationalLimits.LimitTypeKind import LimitTypeKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.OperationalLimits.OperationalLimitDirectionKind import OperationalLimitDirectionKind     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class OperationalLimitType(IdentifiedObject):
    """The operational meaning of a category of limits.
    """
    # The nominal acceptable duration of the limit.  Limits are commonly expressed in
    # terms of the a time limit for which the limit is normally acceptable.   The
    # actual acceptable duration of a specific limit may depend on other local
    # factors such as temperature or wind speed.
    acceptableDuration: Seconds  = None
 
    # Types of limits defined in the ENTSO-E Operational Handbook Policy 3.
    limitType: LimitTypeKind  = None
 
    # The direction of the limit.
    direction: OperationalLimitDirectionKind  = None
     