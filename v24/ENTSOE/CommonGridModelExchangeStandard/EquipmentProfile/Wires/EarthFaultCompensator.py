from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class EarthFaultCompensator(ConductingEquipment):
    """A conducting equipment used to represent a connection to ground which is
    typically used to compensate earth faults..   An earth fault compensator device
    modeled with a single terminal implies a second terminal solidly connected to
    ground.  If two terminals are modeled, the ground is not assumed and normal
    connection rules apply.
    """
    # Nominal resistance of device.
    r_: Resistance  = None
     