from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.AngleRadians import AngleRadians     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Reactance import Reactance     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConductingEquipment import ConductingEquipment
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.EnergySchedulingType import EnergySchedulingType     

@dataclass
class EnergySource(ConductingEquipment):
    """A generic equivalent for an energy supplier on a transmission or distribution
    voltage level.
    """
    # Phase-to-phase nominal voltage.
    nominalVoltage_: Voltage  = None
 
    # Positive sequence Thevenin resistance.
    r_: Resistance  = None
 
    # Zero sequence Thevenin resistance.
    r0_: Resistance  = None
 
    # Negative sequence Thevenin resistance.
    rn_: Resistance  = None
 
    # Phase angle of a-phase open circuit.
    voltageAngle_: AngleRadians  = None
 
    # Phase-to-phase open circuit voltage magnitude.
    voltageMagnitude_: Voltage  = None
 
    # Positive sequence Thevenin reactance.
    x_: Reactance  = None
 
    # Zero sequence Thevenin reactance.
    x0_: Reactance  = None
 
    # Negative sequence Thevenin reactance.
    xn_: Reactance  = None
 
    # Energy Scheduling Type of an Energy Source
    EnergySchedulingType_: Optional[EnergySchedulingType] = None
     