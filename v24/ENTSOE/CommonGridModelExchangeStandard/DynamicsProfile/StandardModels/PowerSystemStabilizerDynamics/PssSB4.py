from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class PssSB4(PowerSystemStabilizerDynamics):
    """Power sensitive stabilizer model.
    """
    # Time constant (Tt).
    tt_: Seconds  = None
 
    # Gain (Kx).
    kx_: PU  = None
 
    # Time constant (Tx2).
    tx2_: Seconds  = None
 
    # Time constant (Ta).
    ta_: Seconds  = None
 
    # Reset time constant (Tx1).
    tx1_: Seconds  = None
 
    # Time constant (Tb).
    tb_: Seconds  = None
 
    # Time constant (Tc).
    tc_: Seconds  = None
 
    # Time constant (Td).
    td_: Seconds  = None
 
    # Time constant (Te).
    te_: Seconds  = None
 
    # Limiter (Vsmax).
    vsmax_: PU  = None
 
    # Limiter (Vsmin).
    vsmin_: PU  = None
     