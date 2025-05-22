from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.DC.DCBaseTerminal import DCBaseTerminal

@dataclass
class DCTerminal(DCBaseTerminal):
    """An electrical connection point to generic DC conducting equipment.
    """
    pass
