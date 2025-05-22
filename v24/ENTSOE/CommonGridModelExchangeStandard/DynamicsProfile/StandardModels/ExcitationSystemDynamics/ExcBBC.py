from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcBBC(ExcitationSystemDynamics):
    """Transformer fed static excitation system (static with ABB regulator). This
    model represents a static excitation system in which a gated thyristor bridge
    fed by a transformer at the main generator terminals feeds the main generator
    directly.
    """
    # Controller time constant (T1).  Typical Value = 6.
    t1_: Seconds  = None
 
    # Controller time constant (T2).  Typical Value = 1.
    t2_: Seconds  = None
 
    # Lead/lag time constant (T3).  Typical Value = 0.05.
    t3_: Seconds  = None
 
    # Lead/lag time constant (T4).  Typical Value = 0.01.
    t4_: Seconds  = None
 
    # Steady state gain (K).  Typical Value = 300.
    k_: PU  = None
 
    # Minimum control element output (Vrmin).  Typical Value = -5.
    vrmin_: PU  = None
 
    # Maximum control element output (Vrmax).  Typical Value = 5.
    vrmax_: PU  = None
 
    # Minimum open circuit exciter voltage (Efdmin).  Typical Value = -5.
    efdmin_: PU  = None
 
    # Maximum open circuit exciter voltage (Efdmax).  Typical Value = 5.
    efdmax_: PU  = None
 
    # Effective excitation transformer reactance (Xe).  Typical Value = 0.05.
    xe_: PU  = None
 
    # Supplementary signal routing selector (switch).
    # true = Vs connected to 3rd summing point
    # false =  Vs connected to 1st summing point (see diagram).
    # Typical Value = true.
    switch_: bool  = None
     