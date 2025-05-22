from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class VsQpccControlKind(Enum):
    reactivePcc = auto()
    voltagePcc = auto()
    powerFactorPcc = auto()