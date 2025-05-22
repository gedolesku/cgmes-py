from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject

@dataclass
class EnergySchedulingType(IdentifiedObject):
    """Used to define the type of generation for scheduling purposes.
    """
    pass
