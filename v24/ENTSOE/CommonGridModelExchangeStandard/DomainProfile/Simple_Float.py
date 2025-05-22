from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Float import Float     

@dataclass
class Simple_Float:
    """A floating point number. The range is unspecified and not limited.
    """
    value: float  = None
     