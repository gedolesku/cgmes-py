from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class LimitSet(IdentifiedObject):
    """Specifies a set of Limits that are associated with a Measurement. A Measurement
    may have several LimitSets corresponding to seasonal or other changing
    conditions. The condition is captured in the name and description attributes.
    The same LimitSet may be used for several Measurements. In particular
    percentage limits are used this way.
    """
    # Tells if the limit values are in percentage of normalValue or the specified
    # Unit for Measurements and Controls.
    isPercentageLimits_: bool  = None
     