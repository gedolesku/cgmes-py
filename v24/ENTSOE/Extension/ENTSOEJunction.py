from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.Extension.BoundaryExtensions import BoundaryExtensions

@dataclass
class ENTSOEJunction(BoundaryExtensions):
    """This is a class extension of the class Junction in CIM. The extension is done
    for the purpose of ENTSO-E profiling work.
    """
    pass
