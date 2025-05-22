from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.CurrentFlow import CurrentFlow     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
from ENTSOE.CommonGridModelExchangeStandard.StateVariablesProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class ACDCConverter(ConductingEquipment):
    """A unit with valves for three phases, together with unit control equipment,
    essential protective and switching devices, DC storage capacitors, phase
    reactors and auxiliaries, if any, used for conversion.
    """
    # Converter DC current, also called Id. Converter state variable, result from
    # power flow.
    idc_: CurrentFlow  = None
 
    # The active power loss at a DC Pole
    # = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2
    # For lossless operation Pdc=Pac
    # For rectifier operation with losses Pdc=Pac-lossP
    # For inverter operation with losses Pdc=Pac+lossP
    # Converter state variable used in power flow.
    poleLossP_: ActivePower  = None
 
    # Converter voltage, the voltage at the AC side of the bridge. Converter state
    # variable, result from power flow.
    uc_: Voltage  = None
 
    # Converter voltage at the DC side, also called Ud. Converter state variable,
    # result from power flow.
    udc_: Voltage  = None
     