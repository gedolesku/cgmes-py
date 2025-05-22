from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class PssSB4(PowerSystemStabilizerDynamics):
    """Power sensitive stabilizer model.
    """
    # Time constant (Tt).
    tt: Seconds  = None
 
    # Gain (Kx).
    kx: PU  = None
 
    # Time constant (Tx2).
    tx2: Seconds  = None
 
    # Time constant (Ta).
    ta: Seconds  = None
 
    # Reset time constant (Tx1).
    tx1: Seconds  = None
 
    # Time constant (Tb).
    tb: Seconds  = None
 
    # Time constant (Tc).
    tc: Seconds  = None
 
    # Time constant (Td).
    td: Seconds  = None
 
    # Time constant (Te).
    te: Seconds  = None
 
    # Limiter (Vsmax).
    vsmax: PU  = None
 
    # Limiter (Vsmin).
    vsmin: PU  = None
     