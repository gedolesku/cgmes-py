from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class PowerSystemResource(IdentifiedObject):
    """A power system resource can be an item of equipment such as a switch, an
    equipment container containing many individual items of equipment such as a
    substation, or an organisational entity such as sub-control area. Power system
    resources can have measurements associated.
    """
    pass
