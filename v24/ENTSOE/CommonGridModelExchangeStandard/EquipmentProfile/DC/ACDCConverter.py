from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ApparentPower import ApparentPower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePowerPerCurrentFlow import ActivePowerPerCurrentFlow     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Terminal import Terminal     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class ACDCConverter(ConductingEquipment):
    """A unit with valves for three phases, together with unit control equipment,
    essential protective and switching devices, DC storage capacitors, phase
    reactors and auxiliaries, if any, used for conversion.
    """
    # Base apparent power of the converter pole.
    baseS: ApparentPower  = None
 
    # Active power loss in pole at no power transfer. Converter configuration data
    # used in power flow.
    idleLoss: ActivePower  = None
 
    # The maximum voltage on the DC side at which the converter should operate.
    # Converter configuration data used in power flow.
    maxUdc: Voltage  = None
 
    # Min allowed converter DC voltage. Converter configuration data used in power
    # flow.
    minUdc: Voltage  = None
 
    # Number of valves in the converter. Used in loss calculations.
    numberOfValves: int  = None
 
    # Rated converter DC voltage, also called UdN. Converter configuration data used
    # in power flow.
    ratedUdc: Voltage  = None
 
    # Converter configuration data used in power flow. Refer to poleLossP.
    resistiveLoss: Resistance  = None
 
    # Switching losses, relative to the base apparent power 'baseS'.
    # Refer to poleLossP.
    switchingLoss: ActivePowerPerCurrentFlow  = None
 
    # Valve threshold voltage. Forward voltage drop when the valve is conducting.
    # Used in loss calculations, i.e. the switchLoss depend on numberOfValves *
    # valveU0.
    valveU0: Voltage  = None
 
    # All converters' DC sides linked to this point of common coupling terminal.
    PccTerminal_ref: Optional[Terminal] = None
    PccTerminal: str = None
     