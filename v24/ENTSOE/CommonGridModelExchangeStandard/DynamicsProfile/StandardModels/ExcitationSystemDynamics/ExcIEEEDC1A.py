from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEDC1A(ExcitationSystemDynamics):
    """The class represents IEEE Std 421.5-2005 type DC1A model. This model represents
    field-controlled dc commutator exciters with continuously acting voltage
    regulators (especially the direct-acting rheostatic, rotating amplifier, and
    magnetic amplifier types).  Because this model has been widely implemented by
    the industry, it is sometimes used to represent other types of systems when
    detailed data for them are not available or when a simplified model is required.
    
    
    
      Reference: IEEE Standard 421.5-2005 Section 5.1.
    """
    # Voltage regulator gain (K<sub>A</sub>).  Typical Value = 46.
    ka_: PU  = None
 
    # Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.06.
    ta_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>B</sub>).  Typical Value = 0.
    tb_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>C</sub>).  Typical Value = 0.
    tc_: Seconds  = None
 
    # Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 1.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -0.9.
    vrmin_: PU  = None
 
    # Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
    # = 0.
    ke_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control
    # (T<sub>E</sub>).  Typical Value = 0.46.
    te_: Seconds  = None
 
    # Excitation control system stabilizer gain (K<sub>F</sub>).  Typical Value = 0.1.
    kf_: PU  = None
 
    # Excitation control system stabilizer time constant (T<sub>F</sub>).  Typical
    # Value = 1.
    tf_: Seconds  = None
 
    # Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>).
    # Typical Value = 3.1.
    efd1_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]).  Typical Value = 0.33.
    seefd1_: Simple_Float  = None
 
    # Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>).
    # Typical Value = 2.3.
    efd2_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]).  Typical Value = 0.1.
    seefd2_: Simple_Float  = None
 
    # UEL input (uelin).
    # true = input is connected to the HV gate
    # false = input connects to the error signal.
    # Typical Value = true.
    uelin_: bool  = None
 
    # (exclim).  IEEE standard is ambiguous about lower limit on exciter output.
    # true = a lower limit of zero is applied to integrator output
    # false = a lower limit of zero is not applied to integrator output.
    # Typical Value = true.
    exclim_: bool  = None
     