from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Reactance import Reactance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.VoltagePerReactivePower import VoltagePerReactivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.SVCControlMode import SVCControlMode     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.RegulatingCondEq import RegulatingCondEq

@dataclass
class StaticVarCompensator(RegulatingCondEq):
    """A facility for providing variable and controllable shunt reactive power. The
    SVC typically consists of a stepdown transformer, filter, thyristor-controlled
    reactor, and thyristor-switched capacitor arms.
    
      The SVC may operate in fixed MVar output mode or in voltage control mode.
    When in voltage control mode, the output of the SVC will be proportional to the
    deviation of voltage at the controlled bus from the voltage setpoint.  The SVC
    characteristic slope defines the proportion.  If the voltage at the controlled
    bus is equal to the voltage setpoint, the SVC MVar output is zero.
    """
    # Maximum available capacitive reactance.
    capacitiveRating_: Reactance  = None
 
    # Maximum available inductive reactance.
    inductiveRating_: Reactance  = None
 
    # The characteristics slope of an SVC defines how the reactive power output
    # changes in proportion to the difference between the regulated bus voltage and
    # the voltage setpoint.
    slope_: VoltagePerReactivePower  = None
 
    # SVC control mode.
    sVCControlMode_: SVCControlMode  = None
 
    # The reactive power output of the SVC is proportional to the difference between
    # the voltage at the regulated bus and the voltage setpoint.  When the regulated
    # bus voltage is equal to the voltage setpoint, the reactive power output is zero.
    voltageSetPoint_: Voltage  = None
     