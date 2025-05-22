from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEDC2A(ExcitationSystemDynamics):
    """The class represents IEEE Std 421.5-2005 type DC2A model. This model represents
    represent field-controlled dc commutator exciters with continuously acting
    voltage regulators having supplies obtained from the generator or auxiliary bus.
     It differs from the Type DC1A model only in the voltage regulator output
    limits, which are now proportional to terminal voltage
    <b>V</b><b><sub>T</sub></b>.
      It is representative of solid-state replacements for various forms of older
    mechanical and rotating amplifier regulating equipment connected to dc
    commutator exciters.
    
      Reference: IEEE Standard 421.5-2005 Section 5.2.
    """
    # Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>).
    # Typical Value = 3.05.
    efd1_: PU  = None
 
    # Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>).
    # Typical Value = 2.29.
    efd2_: PU  = None
 
    # (exclim).  IEEE standard is ambiguous about lower limit on exciter output.
    # Typical Value = - 999  which means that there is no limit applied.
    exclim_: PU  = None
 
    # Voltage regulator gain (K<sub>A</sub>).  Typical Value = 300.
    ka_: PU  = None
 
    # Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
    # = 1.
    ke_: PU  = None
 
    # Excitation control system stabilizer gain (K<sub>F</sub>).  Typical Value = 0.1.
    kf_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]).  Typical Value = 0.279.
    seefd1_: Simple_Float  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]).  Typical Value = 0.117.
    seefd2_: Simple_Float  = None
 
    # Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.01.
    ta_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>B</sub>).  Typical Value = 0.
    tb_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>C</sub>).  Typical Value = 0.
    tc_: Seconds  = None
 
    # Exciter time constant, integration rate associated with exciter control
    # (T<sub>E</sub>).  Typical Value = 1.33.
    te_: Seconds  = None
 
    # Excitation control system stabilizer time constant (T<sub>F</sub>).  Typical
    # Value = 0.675.
    tf_: Seconds  = None
 
    # UEL input (uelin).
    # true = input is connected to the HV gate
    # false = input connects to the error signal.
    # Typical Value = true.
    uelin_: bool  = None
 
    # Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 4.95.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -4.9.
    vrmin_: PU  = None
     