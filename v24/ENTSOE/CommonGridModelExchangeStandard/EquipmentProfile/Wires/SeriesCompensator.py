from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Reactance import Reactance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.CurrentFlow import CurrentFlow     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class SeriesCompensator(ConductingEquipment):
    """A Series Compensator is a series capacitor or reactor or an AC transmission
    line without charging susceptance.  It is a two terminal device.
    """
    # Positive sequence resistance.
    r: Resistance  = None
 
    # Zero sequence resistance.
    r0: Resistance  = None
 
    # Positive sequence reactance.
    x: Reactance  = None
 
    # Zero sequence reactance.
    x0: Reactance  = None
 
    # Describe if a metal oxide varistor (mov) for over voltage protection is
    # configured at the series compensator.
    varistorPresent: bool  = None
 
    # The maximum current the varistor is designed to handle at specified duration.
    varistorRatedCurrent: CurrentFlow  = None
 
    # The dc voltage at which the varistor start conducting.
    varistorVoltageThreshold: Voltage  = None
     