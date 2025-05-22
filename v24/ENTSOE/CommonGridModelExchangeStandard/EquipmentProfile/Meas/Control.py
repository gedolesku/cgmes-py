from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.String import String     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.DateTime import DateTime     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitMultiplier import UnitMultiplier     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitSymbol import UnitSymbol     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.PowerSystemResource import PowerSystemResource     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class Control(IdentifiedObject):
    """Control is used for supervisory/device control. It represents control outputs
    that are used to change the state in a process, e.g. close or open breaker, a
    set point value or a raise lower command.
    """
    # Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint,
    # TieLineFlow etc. The ControlType.name shall be unique among all specified types
    # and describe the type.
    controlType_: str  = None
 
    # Indicates that a client is currently sending control commands that has not
    # completed.
    operationInProgress_: bool  = None
 
    # The last time a control output was sent.
    timeStamp_: DateTime  = None
 
    # The unit multiplier of the controlled quantity.
    unitMultiplier_: UnitMultiplier  = None
 
    # The unit of measure of the controlled quantity.
    unitSymbol_: UnitSymbol  = None
 
    # The controller outputs used to actually govern a regulating device, e.g. the
    # magnetization of a synchronous machine or capacitor bank breaker actuator.
    PowerSystemResource_: Optional[PowerSystemResource] = None
     