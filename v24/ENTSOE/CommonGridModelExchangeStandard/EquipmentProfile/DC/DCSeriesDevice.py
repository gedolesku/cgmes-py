from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Inductance import Inductance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCConductingEquipment import DCConductingEquipment

@dataclass
class DCSeriesDevice(DCConductingEquipment):
    """A series device within the DC system, typically a reactor used for filtering or
    smoothing.  Needed for transient and short circuit studies.
    """
    # Inductance of the device.
    inductance_: Inductance  = None
 
    # Resistance of the DC device.
    resistance_: Resistance  = None
 
    # Rated DC device voltage. Converter configuration data used in power flow.
    ratedUdc_: Voltage  = None
     