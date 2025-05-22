from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class Connector(ConductingEquipment):
    """A conductor, or group of conductors, with negligible impedance, that serve to
    connect other conducting equipment within a single substation and are modelled
    with a single logical terminal.
    """
    pass
