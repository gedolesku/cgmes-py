from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.ShuntCompensator import ShuntCompensator

@dataclass
class LinearShuntCompensator(ShuntCompensator):
    """A linear shunt compensator has banks or sections with equal admittance values.
    """
    pass
