from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEAC2A(ExcitationSystemDynamics):
    """The class represents IEEE Std 421.5-2005 type AC2A model. The model represents
    a high initial response field-controlled alternator-rectifier excitation system.
    The alternator main exciter is used with non-controlled rectifiers. The Type
    AC2A model is similar to that of Type AC1A except for the inclusion of exciter
    time constant compensation and exciter field current limiting elements.
    
      Reference: IEEE Standard 421.5-2005 Section 6.2.
    """
    # Voltage regulator time constant (T<sub>B</sub>).  Typical Value = 0.
    tb_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>C</sub>).  Typical Value = 0.
    tc_: Seconds  = None
 
    # Voltage regulator gain (K<sub>A</sub>).  Typical Value = 400.
    ka_: PU  = None
 
    # Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.02.
    ta_: Seconds  = None
 
    # Maximum voltage regulator output (V<sub>AMAX</sub>).  Typical Value = 8.
    vamax_: PU  = None
 
    # Minimum voltage regulator output (V<sub>AMIN</sub>).  Typical Value = -8.
    vamin_: PU  = None
 
    # Second stage regulator gain (K<sub>B</sub>).  Typical Value = 25.
    kb_: PU  = None
 
    # Maximum voltage regulator outputs (V<sub>RMAX</sub>).  Typical Value = 105.
    vrmax_: PU  = None
 
    # Minimum voltage regulator outputs (V<sub>RMIN</sub>).  Typical Value = -95.
    vrmin_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control
    # (T<sub>E</sub>).  Typical Value = 0.6.
    te_: Seconds  = None
 
    # Exciter field current limit reference (V<sub>FEMAX</sub>).  Typical Value = 4.4.
    vfemax_: PU  = None
 
    # Exciter field current feedback gain (K<sub>H</sub>).  Typical Value = 1.
    kh_: PU  = None
 
    # Excitation control system stabilizer gains (K<sub>F</sub>).  Typical Value = 0.
    # 03.
    kf_: PU  = None
 
    # Excitation control system stabilizer time constant (T<sub>F</sub>).  Typical
    # Value = 1.
    tf_: Seconds  = None
 
    # Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>).
    # Typical Value = 0.28.
    kc_: PU  = None
 
    # Demagnetizing factor, a function of exciter alternator reactances
    # (K<sub>D</sub>).  Typical Value = 0.35.
    kd_: PU  = None
 
    # Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
    # = 1.
    ke_: PU  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (V<sub>E1</sub>).  Typical Value = 4.4.
    ve1_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]).
    # Typical Value = 0.037.
    seve1_: Simple_Float  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (V<sub>E2</sub>).  Typical Value = 3.3.
    ve2_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]).
    # Typical Value = 0.012.
    seve2_: Simple_Float  = None
     