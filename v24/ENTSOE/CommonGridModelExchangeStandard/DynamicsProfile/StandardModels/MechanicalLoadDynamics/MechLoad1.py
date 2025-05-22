from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.MechanicalLoadDynamics.MechanicalLoadDynamics import MechanicalLoadDynamics

@dataclass
class MechLoad1(MechanicalLoadDynamics):
    """Mechanical load model type 1.
    """
    # Speed squared coefficient (a).
    a_: Simple_Float  = None
 
    # Speed coefficient (b).
    b_: Simple_Float  = None
 
    # Speed to the exponent coefficient (d).
    d_: Simple_Float  = None
 
    # Exponent (e).
    e_: Simple_Float  = None
     