from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.String import String     
from ENTSOE.CommonGridModelExchangeStandard.DiagramLayoutProfile.DiagramLayout.DiagramObject import DiagramObject

@dataclass
class TextDiagramObject(DiagramObject):
    """A diagram object for placing free-text or text derived from an associated
    domain object.
    """
    # The text that is displayed by this text diagram object.
    text: str  = None
     