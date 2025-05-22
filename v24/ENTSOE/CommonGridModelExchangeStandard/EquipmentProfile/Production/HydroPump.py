from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.RotatingMachine import RotatingMachine     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Equipment import Equipment
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.HydroPowerPlant import HydroPowerPlant     

@dataclass
class HydroPump(Equipment):
    """A synchronous motor-driven pump, typically associated with a pumped storage
    plant.
    """
    # The synchronous machine drives the turbine which moves the water from a low
    # elevation to a higher elevation. The direction of machine rotation for pumping
    # may or may not be the same as for generating.
    RotatingMachine_ref: Optional[RotatingMachine] = None
    RotatingMachine: str = None
 
    # The hydro pump may be a member of a pumped storage plant or a pump for
    # distributing water.
    HydroPowerPlant_ref: Optional[HydroPowerPlant] = None
    HydroPowerPlant: str = None
     