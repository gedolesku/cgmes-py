from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DiagramLayoutProfile.DiagramLayout.Diagram import Diagram     
from ENTSOE.CommonGridModelExchangeStandard.DiagramLayoutProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class DiagramStyle(IdentifiedObject):
    """The diagram style refer to a style used by the originating system for a diagram.
     A diagram style describes information such as schematic, geographic, bus-
    branch etc.
    """
    # A DiagramStyle can be used by many Diagrams.
    Diagram: List[Diagram]  = field(default_factory=list)
     