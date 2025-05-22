from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.EquipmentContainer import EquipmentContainer
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Substation import Substation     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Bay import Bay     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.BaseVoltage import BaseVoltage     

@dataclass
class VoltageLevel(EquipmentContainer):
    """A collection of equipment at one common system voltage forming a switchgear.
    The equipment typically consist of breakers, busbars, instrumentation, control,
    regulation and protection devices as well as assemblies of all these.
    """
    # The bus bar's high voltage limit
    highVoltageLimit_: Voltage  = None
 
    # The bus bar's low voltage limit
    lowVoltageLimit_: Voltage  = None
 
    # The substation of the voltage level.
    Substation_: Optional[Substation] = None
 
    # The bays within this voltage level.
    Bay_: List[Bay]  = field(default_factory=list)
 
    # The base voltage used for all equipment within the voltage level.
    BaseVoltage_: Optional[BaseVoltage] = None
     