from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class DynamicsFunctionBlock(IdentifiedObject):
    """Abstract parent class for all Dynamics function blocks.
    """
    # Function block used indicator.
    # true = use of function block is enabled
    # false = use of function block is disabled.
    enabled_: bool  = None
     