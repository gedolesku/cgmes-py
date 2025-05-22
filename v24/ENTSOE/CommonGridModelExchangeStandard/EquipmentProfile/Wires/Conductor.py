from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Length import Length     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class Conductor(ConductingEquipment):
    """Combination of conducting material with consistent electrical characteristics,
    building a single electrical system, used to carry current between points in
    the power system.
    """
    # Segment length for calculating line section capabilities
    length: Length  = None
     