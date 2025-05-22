from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Equipment import Equipment
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.BaseVoltage import BaseVoltage     

@dataclass
class ConductingEquipment(Equipment):
    """The parts of the AC power system that are designed to carry current or that are
    conductively connected through terminals.
    """
    # All conducting equipment with this base voltage.  Use only when there is no
    # voltage level container used and only one base voltage applies.  For example,
    # not used for transformers.
    BaseVoltage_: Optional[BaseVoltage] = None
     