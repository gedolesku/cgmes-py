from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DiagramLayoutProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class DiagramObjectStyle(IdentifiedObject):
    """A reference to a style used by the originating system for a diagram object.  A
    diagram object style describes information such as line thickness, shape such
    as circle or rectangle etc, and color.
    """
    pass
