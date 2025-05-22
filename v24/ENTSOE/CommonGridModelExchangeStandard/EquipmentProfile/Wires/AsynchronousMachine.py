from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PerCent import PerCent     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Frequency import Frequency     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.RotationSpeed import RotationSpeed     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.RotatingMachine import RotatingMachine

@dataclass
class AsynchronousMachine(RotatingMachine):
    """A rotating machine whose shaft rotates asynchronously with the electrical field.
     Also known as an induction machine with no external connection to the rotor
    windings, e.g squirrel-cage induction machine.
    """
    # Indicates whether the machine is a converter fed drive. Used for short circuit
    # data exchange according to IEC 60909
    converterFedDrive_: bool  = None
 
    # Efficiency of the asynchronous machine at nominal operation in percent.
    # Indicator for converter drive motors. Used for short circuit data exchange
    # according to IEC 60909
    efficiency_: PerCent  = None
 
    # Ratio of locked-rotor current to the rated current of the motor (Ia/Ir). Used
    # for short circuit data exchange according to IEC 60909
    iaIrRatio_: Simple_Float  = None
 
    # Nameplate data indicates if the machine is 50 or 60 Hz.
    nominalFrequency_: Frequency  = None
 
    # Nameplate data.  Depends on the slip and number of pole pairs.
    nominalSpeed_: RotationSpeed  = None
 
    # Number of pole pairs of stator. Used for short circuit data exchange according
    # to IEC 60909
    polePairNumber_: int  = None
 
    # Rated mechanical power (Pr in the IEC 60909-0). Used for short circuit data
    # exchange according to IEC 60909.
    ratedMechanicalPower_: ActivePower  = None
 
    # Indicates for converter drive motors if the power can be reversible. Used for
    # short circuit data exchange according to IEC 60909
    reversible_: bool  = None
 
    # Locked rotor ratio (R/X). Used for short circuit data exchange according to IEC
    # 60909
    rxLockedRotorRatio_: Simple_Float  = None
     