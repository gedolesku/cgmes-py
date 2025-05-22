from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DiagramLayoutProfile.DiagramLayout.DiagramObjectPoint import DiagramObjectPoint     

@dataclass
class DiagramObjectGluePoint:
    """This is used for grouping diagram object points from different diagram objects
    that are considered to be glued together in a diagram even if they are not at
    the exact same coordinates.
    """
    # The 'glue' point to which this point is associated.
    DiagramObjectPoint_: Optional[DiagramObjectPoint] = None
     