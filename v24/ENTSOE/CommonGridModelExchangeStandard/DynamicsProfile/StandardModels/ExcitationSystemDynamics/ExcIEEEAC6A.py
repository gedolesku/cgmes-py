from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEAC6A(ExcitationSystemDynamics):
    """The class represents IEEE Std 421.5-2005 type AC6A model. The model represents
    field-controlled alternator-rectifier excitation systems with system-supplied
    electronic voltage regulators.  The maximum output of the regulator,
    <b><i>V</i></b><b><i><sub>R</sub></i></b>, is a function of terminal voltage,
    <b><i>V</i></b><b><i><sub>T</sub></i></b>. The field current limiter included
    in the original model AC6A remains in the 2005 update.
    
      Reference: IEEE Standard 421.5-2005 Section 6.6.
    """
    # Voltage regulator gain (K<sub>A</sub>).  Typical Value = 536.
    ka_: PU  = None
 
    # Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.086.
    ta_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>K</sub>).  Typical Value = 0.18.
    tk_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>B</sub>).  Typical Value = 9.
    tb_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>C</sub>).  Typical Value = 3.
    tc_: Seconds  = None
 
    # Maximum voltage regulator output (V<sub>AMAX</sub>).  Typical Value = 75.
    vamax_: PU  = None
 
    # Minimum voltage regulator output (V<sub>AMIN</sub>).  Typical Value = -75.
    vamin_: PU  = None
 
    # Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 44.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -36.
    vrmin_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control
    # (T<sub>E</sub>).  Typical Value = 1.
    te_: Seconds  = None
 
    # Exciter field current limiter gain (K<sub>H</sub>).  Typical Value = 92.
    kh_: PU  = None
 
    # Exciter field current limiter time constant (T<sub>J</sub>).  Typical Value = 0.
    # 02.
    tj_: Seconds  = None
 
    # Exciter field current limiter time constant (T<sub>H</sub>).  Typical Value = 0.
    # 08.
    th_: Seconds  = None
 
    # Exciter field current limit reference (V<sub>FELIM</sub>).  Typical Value = 19.
    vfelim_: PU  = None
 
    # Maximum field current limiter signal reference (V<sub>HMAX</sub>).  Typical
    # Value = 75.
    vhmax_: PU  = None
 
    # Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>).
    # Typical Value = 0.173.
    kc_: PU  = None
 
    # Demagnetizing factor, a function of exciter alternator reactances
    # (K<sub>D</sub>).  Typical Value = 1.91.
    kd_: PU  = None
 
    # Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
    # = 1.6.
    ke_: PU  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (V<sub>E1</sub>) equals V<sub>EMAX </sub>(V<sub>E1</sub>).
    #  Typical Value = 7.4.
    ve1_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]).
    # Typical Value = 0.214.
    seve1_: Simple_Float  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (V<sub>E2</sub>).  Typical Value = 5.55.
    ve2_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]).
    # Typical Value = 0.044.
    seve2_: Simple_Float  = None
     