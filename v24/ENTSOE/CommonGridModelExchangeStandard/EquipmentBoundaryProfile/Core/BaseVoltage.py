from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentBoundaryProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class BaseVoltage(IdentifiedObject):
    """Defines a system base voltage which is referenced.
    """
    # The power system resource's base voltage.
    nominalVoltage_: Voltage  = None
     