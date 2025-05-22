from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.Extension.OperationalLimits.LimitTypeKind import LimitTypeKind     

@dataclass
class ENTSOEOperationalLimitType:
    """The extension is described in the ENTSO-E document Policy 3 section 3 and
    appendix to Policy 3.
    """
    # Types of limits defined in the ENTSO-E Operational Handbook Policy 3.
    limitType: LimitTypeKind  = None
     