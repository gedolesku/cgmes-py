from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.StateVariablesProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class DCTopologicalIsland(IdentifiedObject):
    """An electrically connected subset of the network. DC topological islands can
    change as the current network state changes: e.g. due to
      - disconnect switches or breakers change state in a SCADA/EMS
      - manual creation, change or deletion of topological nodes in a planning tool.
    """
    pass
