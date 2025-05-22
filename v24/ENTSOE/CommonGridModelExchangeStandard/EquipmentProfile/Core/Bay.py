from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.VoltageLevel import VoltageLevel     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.EquipmentContainer import EquipmentContainer

@dataclass
class Bay(EquipmentContainer):
    """A collection of power system resources (within a given substation) including
    conducting equipment, protection relays, measurements, and telemetry.  A bay
    typically represents a physical grouping related to modularization of equipment.
    """
    # The voltage level containing this bay.
    VoltageLevel_: Optional[VoltageLevel] = None
     