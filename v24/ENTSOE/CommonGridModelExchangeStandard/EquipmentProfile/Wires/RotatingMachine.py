from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ApparentPower import ApparentPower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.RegulatingCondEq import RegulatingCondEq
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.GeneratingUnit import GeneratingUnit     

@dataclass
class RotatingMachine(RegulatingCondEq):
    """A rotating machine which may be used as a generator or motor.
    """
    # Power factor (nameplate data). It is primarily used for short circuit data
    # exchange according to IEC 60909.
    ratedPowerFactor_: Simple_Float  = None
 
    # Nameplate apparent power rating for the unit.
    # The attribute shall have a positive value.
    ratedS_: ApparentPower  = None
 
    # Rated voltage (nameplate data, Ur in IEC 60909-0). It is primarily used for
    # short circuit data exchange according to IEC 60909.
    ratedU_: Voltage  = None
 
    # A synchronous machine may operate as a generator and as such becomes a member
    # of a generating unit.
    GeneratingUnit_: Optional[GeneratingUnit] = None
     