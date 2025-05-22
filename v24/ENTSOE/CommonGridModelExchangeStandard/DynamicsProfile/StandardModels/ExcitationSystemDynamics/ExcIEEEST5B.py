from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEST5B(ExcitationSystemDynamics):
    """The class represents IEEE Std 421.5-2005 type ST5B model. The Type ST5B
    excitation system is a variation of the Type ST1A model, with alternative
    overexcitation and underexcitation inputs and additional limits.
    
      Reference: IEEE Standard 421.5-2005 Section 7.5.
    
      Note: the block diagram in the IEEE 421.5 standard has input signal Vc and
    does not indicate the summation point with Vref. The implementation of the
    ExcIEEEST5B shall consider summation point with Vref.
    """
    # Regulator gain (K<sub>R</sub>).  Typical Value = 200.
    kr: PU  = None
 
    # Firing circuit time constant (T1).  Typical Value = 0.004.
    t1: Seconds  = None
 
    # Rectifier regulation factor (K<sub>C</sub>).  Typical Value = 0.004.
    kc: PU  = None
 
    # Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 5.
    vrmax: PU  = None
 
    # Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -4.
    vrmin: PU  = None
 
    # Regulator lead time constant (T<sub>C1</sub>).  Typical Value = 0.8.
    tc1: Seconds  = None
 
    # Regulator lag time constant (T<sub>B1</sub>).  Typical Value = 6.
    tb1: Seconds  = None
 
    # Regulator lead time constant (T<sub>C2</sub>).  Typical Value = 0.08.
    tc2: Seconds  = None
 
    # Regulator lag time constant (T<sub>B2</sub>).  Typical Value = 0.01.
    tb2: Seconds  = None
 
    # OEL lead time constant (T<sub>OC1</sub>).  Typical Value = 0.1.
    toc1: Seconds  = None
 
    # OEL lag time constant (T<sub>OB1</sub>).  Typical Value = 2.
    tob1: Seconds  = None
 
    # OEL lead time constant (T<sub>OC2</sub>).  Typical Value = 0.08.
    toc2: Seconds  = None
 
    # OEL lag time constant (T<sub>OB2</sub>).  Typical Value = 0.08.
    tob2: Seconds  = None
 
    # UEL lead time constant (T<sub>UC1</sub>).  Typical Value = 2.
    tuc1: Seconds  = None
 
    # UEL lag time constant (T<sub>UB1</sub>).  Typical Value = 10.
    tub1: Seconds  = None
 
    # UEL lead time constant (T<sub>UC2</sub>).  Typical Value = 0.1.
    tuc2: Seconds  = None
 
    # UEL lag time constant (T<sub>UB2</sub>).  Typical Value = 0.05.
    tub2: Seconds  = None
     