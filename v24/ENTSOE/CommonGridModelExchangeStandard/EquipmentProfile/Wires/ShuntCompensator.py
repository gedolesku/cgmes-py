from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.DateTime import DateTime     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.VoltagePerReactivePower import VoltagePerReactivePower     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.RegulatingCondEq import RegulatingCondEq

@dataclass
class ShuntCompensator(RegulatingCondEq):
    """A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors.
    A section of a shunt compensator is an individual capacitor or reactor.  A
    negative value for reactivePerSection indicates that the compensator is a
    reactor. ShuntCompensator is a single terminal device.  Ground is implied.
    """
    # Time delay required for the device to be connected or disconnected by automatic
    # voltage regulation (AVR).
    aVRDelay: Seconds  = None
 
    # Used for Yn and Zn connections. True if the neutral is solidly grounded.
    grounded: bool  = None
 
    # The maximum number of sections that may be switched in. 
    maximumSections: int  = None
 
    # The voltage at which the nominal reactive power may be calculated. This should
    # normally be within 10% of the voltage at which the capacitor is connected to
    # the network.
    nomU: Voltage  = None
 
    # The normal number of sections switched in.
    normalSections: int  = None
 
    # The switch on count since the capacitor count was last reset or initialized.
    switchOnCount: int  = None
 
    # The date and time when the capacitor bank was last switched on.
    switchOnDate: DateTime  = None
 
    # Voltage sensitivity required for the device to regulate the bus voltage, in
    # voltage/reactive power.
    voltageSensitivity: VoltagePerReactivePower  = None
     