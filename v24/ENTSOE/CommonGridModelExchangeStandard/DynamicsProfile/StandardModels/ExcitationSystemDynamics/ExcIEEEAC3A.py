from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEAC3A(ExcitationSystemDynamics):
    """The class represents IEEE Std 421.5-2005 type AC3A model. The model represents
    the field-controlled alternator-rectifier excitation systems designated Type
    AC3A. These excitation systems include an alternator main exciter with non-
    controlled rectifiers. The exciter employs self-excitation, and the voltage
    regulator power is derived from the exciter output voltage.  Therefore, this
    system has an additional nonlinearity, simulated by the use of a multiplier
      whose inputs are the voltage regulator command signal, <b>Va</b>, and the
    exciter output voltage, <b>Efd</b>, times <b>K</b><b><sub>R</sub></b>.  This
    model is applicable to excitation systems employing static voltage regulators.
    
    
      Reference: IEEE Standard 421.5-2005 Section 6.3.
    """
    # Voltage regulator time constant (T<sub>B</sub>).  Typical Value = 0.
    tb_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>C</sub>).  Typical Value = 0.
    tc_: Seconds  = None
 
    # Voltage regulator gain (K<sub>A</sub>).  Typical Value = 45.62.
    ka_: PU  = None
 
    # Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.013.
    ta_: Seconds  = None
 
    # Maximum voltage regulator output (V<sub>AMAX</sub>).  Typical Value = 1.
    vamax_: PU  = None
 
    # Minimum voltage regulator output (V<sub>AMIN</sub>).  Typical Value = -0.95.
    vamin_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control
    # (T<sub>E</sub>).  Typical Value = 1.17.
    te_: Seconds  = None
 
    # Minimum exciter voltage output (V<sub>EMIN</sub>).  Typical Value = 0.1.
    vemin_: PU  = None
 
    # Constant associated with regulator and alternator field power supply
    # (K<sub>R</sub>).  Typical Value = 3.77.
    kr_: PU  = None
 
    # Excitation control system stabilizer gains (K<sub>F</sub>).  Typical Value = 0.
    # 143.
    kf_: PU  = None
 
    # Excitation control system stabilizer time constant (T<sub>F</sub>).  Typical
    # Value = 1.
    tf_: Seconds  = None
 
    # Excitation control system stabilizer gain (K<sub>N</sub>).  Typical Value = 0.
    # 05.
    kn_: PU  = None
 
    # Value of <i>EFD </i>at which feedback gain changes (E<sub>FDN</sub>).  Typical
    # Value = 2.36.
    efdn_: PU  = None
 
    # Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>).
    # Typical Value = 0.104.
    kc_: PU  = None
 
    # Demagnetizing factor, a function of exciter alternator reactances
    # (K<sub>D</sub>).  Typical Value = 0.499.
    kd_: PU  = None
 
    # Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
    # = 1.
    ke_: PU  = None
 
    # Exciter field current limit reference (V<sub>FEMAX</sub>).  Typical Value = 16.
    vfemax_: PU  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (V<sub>E1</sub>) equals V<sub>EMAX </sub>(V<sub>E1</sub>).
    #  Typical Value = 6.24.
    ve1_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]).
    # Typical Value = 1.143.
    seve1_: Simple_Float  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (V<sub>E2</sub>).  Typical Value = 4.68.
    ve2_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]).
    # Typical Value = 0.1.
    seve2_: Simple_Float  = None
     