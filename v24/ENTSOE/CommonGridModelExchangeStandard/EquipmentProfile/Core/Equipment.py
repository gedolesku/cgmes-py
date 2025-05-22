from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.EquipmentContainer import EquipmentContainer     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.PowerSystemResource import PowerSystemResource

@dataclass
class Equipment(PowerSystemResource):
    """The parts of a power system that are physical devices, electronic or mechanical.
    """
    # The single instance of equipment represents multiple pieces of equipment that
    # have been modeled together as an aggregate.  Examples would be power
    # transformers or synchronous machines operating in parallel modeled as a single
    # aggregate power transformer or aggregate synchronous machine.  This is not to
    # be used to indicate equipment that is part of a group of interdependent
    # equipment produced by a network production program.  
    aggregate_: bool  = None
 
    # Container of this equipment.
    EquipmentContainer_: Optional[EquipmentContainer] = None
     