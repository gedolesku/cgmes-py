from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.ShuntCompensator import ShuntCompensator

@dataclass
class NonlinearShuntCompensator(ShuntCompensator):
    """A non linear shunt compensator has bank or section admittance values that
    differs.
    """
    pass
