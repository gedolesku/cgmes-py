from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcHU(ExcitationSystemDynamics):
    """Hungarian Excitation System Model, with built-in voltage transducer.
    """
    # Filter time constant (Tr). If a voltage compensator is used in conjunction with
    # this excitation system model, Tr should be set to 0.  Typical Value = 0.01.
    tr: Seconds  = None
 
    # Major loop PI tag integration time constant (Te).  Typical Value = 0.154.
    te: Seconds  = None
 
    # Major loop PI tag output signal lower limit (Imin).  Typical Value = 0.1.
    imin: PU  = None
 
    # Major loop PI tag output signal upper limit (Imax).  Typical Value = 2.19.
    imax: PU  = None
 
    # Major loop PI tag gain factor (Ae).  Typical Value = 3.
    ae: PU  = None
 
    # Field voltage control signal lower limit on AVR base (Emin).  Typical Value = -
    # 0.866.
    emin: PU  = None
 
    # Field voltage control signal upper limit on AVR base (Emax).  Typical Value = 0.
    # 996.
    emax: PU  = None
 
    # Current base conversion constant (Ki).  Typical Value = 0.21428.
    ki: Simple_Float  = None
 
    # Minor loop PI tag gain factor (Ai).  Typical Value = 22.
    ai: PU  = None
 
    # Minor loop PI control tag integration time constant (Ti).  Typical Value = 0.
    # 01333.
    ti: Seconds  = None
 
    # AVR constant (Atr).  Typical Value = 2.19.
    atr: PU  = None
 
    # Voltage base conversion constant (Ke).  Typical Value = 4.666.
    ke: Simple_Float  = None
     