from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Reactance import Reactance     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.EarthFaultCompensator import EarthFaultCompensator

@dataclass
class GroundingImpedance(EarthFaultCompensator):
    """A fixed impedance device used for grounding.
    """
    # Reactance of device.
    x_: Reactance  = None
     