from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Equipment import Equipment     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ACDCTerminal import ACDCTerminal     

@dataclass
class OperationalLimitSet(IdentifiedObject):
    """A set of limits associated with equipment.  Sets of limits might apply to a
    specific temperature, or season for example. A set of limits may contain
    different severities of limit levels that would apply to the same equipment.
    The set may contain limits of different types such as apparent power and
    current limits or high and low voltage limits  that are logically applied
    together as a set.
    """
    # The equipment to which the limit set applies.
    Equipment_: Optional[Equipment] = None
 
    ACDCTerminal_: Optional[ACDCTerminal] = None
     