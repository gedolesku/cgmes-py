from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.StateVariablesProfile.Core.ACDCTerminal import ACDCTerminal

@dataclass
class Terminal(ACDCTerminal):
    """An AC electrical connection point to a piece of conducting equipment. Terminals
    are connected at physical connection points called connectivity nodes.
    """
    pass
