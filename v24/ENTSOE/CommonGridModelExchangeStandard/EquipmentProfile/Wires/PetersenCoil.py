from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.PetersenCoilModeKind import PetersenCoilModeKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.CurrentFlow import CurrentFlow     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Reactance import Reactance     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.EarthFaultCompensator import EarthFaultCompensator

@dataclass
class PetersenCoil(EarthFaultCompensator):
    """A tunable impedance device normally used to offset line charging during single
    line faults in an ungrounded section of network.
    """
    # The mode of operation of the Petersen coil.
    mode_: PetersenCoilModeKind  = None
 
    # The nominal voltage for which the coil is designed.
    nominalU_: Voltage  = None
 
    # The offset current that the Petersen coil controller is operating from the
    # resonant point.  This is normally a fixed amount for which the controller is
    # configured and could be positive or negative.  Typically 0 to 60 Amperes
    # depending on voltage and resonance conditions.
    offsetCurrent_: CurrentFlow  = None
 
    # The control current used to control the Petersen coil also known as the
    # position current.  Typically in the range of 20-200mA.
    positionCurrent_: CurrentFlow  = None
 
    # The maximum reactance. 
    xGroundMax_: Reactance  = None
 
    # The minimum reactance.
    xGroundMin_: Reactance  = None
 
    # The nominal reactance.  This is the operating point (normally over
    # compensation) that is defined based on the resonance point in the healthy
    # network condition.  The impedance is calculated based on nominal voltage
    # divided by position current.
    xGroundNominal_: Reactance  = None
     