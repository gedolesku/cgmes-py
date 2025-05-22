from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.GeneratingUnit import GeneratingUnit     

@dataclass
class ControlAreaGeneratingUnit(IdentifiedObject):
    """A control area generating unit. This class is needed so that alternate control
    area definitions may include the same generating unit.   Note only one instance
    within a control area should reference a specific generating unit.
    """
    # The generating unit specified for this control area.  Note that a control area
    # should include a GeneratingUnit only once.
    GeneratingUnit_: Optional[GeneratingUnit] = None
     