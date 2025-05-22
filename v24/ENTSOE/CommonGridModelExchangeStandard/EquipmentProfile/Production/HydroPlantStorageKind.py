from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class HydroPlantStorageKind(Enum):
    """The type of hydro power plant.
    """
    # Run of river.
    runOfRiver = auto()
    # Pumped storage.
    pumpedStorage = auto()
    # Storage.
    storage = auto()