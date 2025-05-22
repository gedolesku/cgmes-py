from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcST1A(ExcitationSystemDynamics):
    """Modification of an old IEEE ST1A static excitation system without
    overexcitation limiter (OEL) and underexcitation limiter (UEL).
    """
    # Maximum voltage regulator input limit (Vimax).  Typical Value = 999.
    vimax_: PU  = None
 
    # Minimum voltage regulator input limit (Vimin).  Typical Value = -999.
    vimin_: PU  = None
 
    # Voltage regulator time constant (Tc).  Typical Value = 1.
    tc_: Seconds  = None
 
    # Voltage regulator time constant (Tb).  Typical Value = 10.
    tb_: Seconds  = None
 
    # Voltage regulator gain (Ka).  Typical Value = 190.
    ka_: PU  = None
 
    # Voltage regulator time constant (Ta).  Typical Value = 0.02.
    ta_: Seconds  = None
 
    # Maximum voltage regulator outputs (Vrmax).  Typical Value = 7.8.
    vrmax_: PU  = None
 
    # Minimum voltage regulator outputs (Vrmin).  Typical Value = -6.7.
    vrmin_: PU  = None
 
    # Rectifier loading factor proportional to commutating reactance (Kc). Typical
    # Value = 0.05.
    kc_: PU  = None
 
    # Excitation control system stabilizer gains (Kf).  Typical Value = 0.
    kf_: PU  = None
 
    # Excitation control system stabilizer time constant (Tf).  Typical Value = 1.
    tf_: Seconds  = None
 
    # Voltage regulator time constant (Tc<sub>1</sub>).  Typical Value = 0.
    tc1_: Seconds  = None
 
    # Voltage regulator time constant (Tb<sub>1</sub>).  Typical Value = 0.
    tb1_: Seconds  = None
 
    # Maximum voltage regulator output (Vamax).  Typical Value = 999.
    vamax_: PU  = None
 
    # Minimum voltage regulator output (Vamin).  Typical Value = -999.
    vamin_: PU  = None
 
    # Exciter output current limit reference (Ilr).  Typical Value = 0.
    ilr_: PU  = None
 
    # Exciter output current limiter gain (Klr).  Typical Value = 0.
    klr_: PU  = None
 
    # Excitation xfmr effective reactance (Xe).  Typical Value = 0.04.
    xe_: PU  = None
     