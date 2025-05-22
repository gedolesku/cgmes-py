from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.GeneratingUnit import GeneratingUnit

@dataclass
class SolarGeneratingUnit(GeneratingUnit):
    """A solar thermal generating unit.
    """
    pass
