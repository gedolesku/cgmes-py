from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcSEXS(ExcitationSystemDynamics):
    """Simplified Excitation System Model.
    """
    # Ta/Tb - gain reduction ratio of lag-lead element (TaTb).  Typical Value = 0.1.
    tatb_: Simple_Float  = None
 
    # Denominator time constant of lag-lead block (Tb).  Typical Value = 10.
    tb_: Seconds  = None
 
    # Gain (K) (>0).  Typical Value = 100.
    k_: PU  = None
 
    # Time constant of gain block (Te).  Typical Value = 0.05.
    te_: Seconds  = None
 
    # Minimum field voltage output (Emin).  Typical Value = -5.
    emin_: PU  = None
 
    # Maximum field voltage output (Emax).  Typical Value = 5.
    emax_: PU  = None
 
    # PI controller gain (Kc).  Typical Value = 0.08.
    kc_: PU  = None
 
    # PI controller phase lead time constant (Tc).  Typical Value = 0.
    tc_: Seconds  = None
 
    # Field voltage clipping minimum limit (Efdmin).  Typical Value = -5.
    efdmin_: PU  = None
 
    # Field voltage clipping maximum limit (Efdmax).  Typical Value = 5.
    efdmax_: PU  = None
     