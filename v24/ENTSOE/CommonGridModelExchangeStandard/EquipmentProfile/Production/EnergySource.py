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
    nominalVoltage: Voltage  = None
 
    # Positive sequence Thevenin resistance.
    r: Resistance  = None
 
    # Zero sequence Thevenin resistance.
    r0: Resistance  = None
 
    # Negative sequence Thevenin resistance.
    rn: Resistance  = None
 
    # Phase angle of a-phase open circuit.
    voltageAngle: AngleRadians  = None
 
    # Phase-to-phase open circuit voltage magnitude.
    voltageMagnitude: Voltage  = None
 
    # Positive sequence Thevenin reactance.
    x: Reactance  = None
 
    # Zero sequence Thevenin reactance.
    x0: Reactance  = None
 
    # Negative sequence Thevenin reactance.
    xn: Reactance  = None
 
    # Energy Scheduling Type of an Energy Source
    EnergySchedulingType_ref: Optional[EnergySchedulingType] = None
    EnergySchedulingType: str = None
     