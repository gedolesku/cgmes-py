from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcAC4A(ExcitationSystemDynamics):
    """Modified IEEE AC4A alternator-supplied rectifier excitation system with
    different minimum controller output.
    """
    # Maximum voltage regulator input limit (Vimax).  Typical Value = 10.
    vimax: PU  = None
 
    # Minimum voltage regulator input limit (Vimin).  Typical Value = -10.
    vimin: PU  = None
 
    # Voltage regulator time constant (Tc).  Typical Value = 1.
    tc: Seconds  = None
 
    # Voltage regulator time constant (Tb).  Typical Value = 10.
    tb: Seconds  = None
 
    # Voltage regulator gain (Ka).  Typical Value = 200.
    ka: PU  = None
 
    # Voltage regulator time constant (Ta).  Typical Value = 0.015.
    ta: Seconds  = None
 
    # Maximum voltage regulator output (Vrmax).  Typical Value = 5.64.
    vrmax: PU  = None
 
    # Minimum voltage regulator output (Vrmin).  Typical Value = -4.53.
    vrmin: PU  = None
 
    # Rectifier loading factor proportional to commutating reactance (Kc).  Typical
    # Value = 0.
    kc: PU  = None
     