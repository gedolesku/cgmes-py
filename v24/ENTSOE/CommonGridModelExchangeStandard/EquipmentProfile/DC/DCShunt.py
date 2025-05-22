from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Capacitance import Capacitance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCConductingEquipment import DCConductingEquipment

@dataclass
class DCShunt(DCConductingEquipment):
    """A shunt device within the DC system, typically used for filtering.  Needed for
    transient and short circuit studies.
    """
    # Capacitance of the DC shunt.
    capacitance_: Capacitance  = None
 
    # Resistance of the DC device.
    resistance_: Resistance  = None
 
    # Rated DC device voltage. Converter configuration data used in power flow.
    ratedUdc_: Voltage  = None
     