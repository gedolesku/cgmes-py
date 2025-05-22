from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcSCRX(ExcitationSystemDynamics):
    """Simple excitation system model representing generic characteristics of many
    excitation systems; intended for use where negative field current may be a
    problem.
    """
    # Ta/Tb - gain reduction ratio of lag-lead element (TaTb). The parameter Ta is
    # not defined explicitly.  Typical Value = 0.1.
    tatb_: Simple_Float  = None
 
    # Denominator time constant of lag-lead block (Tb).  Typical Value = 10.
    tb_: Seconds  = None
 
    # Gain (K) (>0).  Typical Value = 200.
    k_: PU  = None
 
    # Time constant of gain block (Te) (>0).  Typical Value = 0.02.
    te_: Seconds  = None
 
    # Minimum field voltage output (Emin).  Typical Value = 0.
    emin_: PU  = None
 
    # Maximum field voltage output (Emax).  Typical Value = 5.
    emax_: PU  = None
 
    # Power source switch (Cswitch).
    # true = fixed voltage of 1.0 PU
    # false = generator terminal voltage.
    cswitch_: bool  = None
 
    # Rc/Rfd - ratio of field discharge resistance to field winding resistance
    # (RcRfd).  Typical Value = 0.
    rcrfd_: Simple_Float  = None
     