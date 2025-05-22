from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.Switch import Switch

@dataclass
class Disconnector(Switch):
    """A manually operated or motor operated mechanical switching device used for
    changing the connections in a circuit, or for isolating a circuit or equipment
    from a source of power. It is required to open or close circuits when
    negligible current is broken or made.
    """
    pass
