from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardInterconnections.RemoteInputSignal import RemoteInputSignal     

@dataclass
class WindPlantDynamics(DynamicsFunctionBlock):
    """Parent class supporting relationships to wind turbines Type 3 and 4 and wind
    plant IEC and user defined wind plants including their control models.
    """
    # The wind plant using the remote signal.
    RemoteInputSignal_ref: Optional[RemoteInputSignal] = None
    RemoteInputSignal: str = None
     