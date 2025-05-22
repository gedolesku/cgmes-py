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
class ExcIEEEDC4B(ExcitationSystemDynamics):
    """The class represents IEEE Std 421.5-2005 type DC4B model. These excitation
    systems utilize a field-controlled dc commutator exciter with a continuously
    acting voltage regulator having supplies obtained from the generator or
    auxiliary bus.
    
      Reference: IEEE Standard 421.5-2005 Section 5.4.
    """
    # Voltage regulator gain (K<sub>A</sub>).  Typical Value = 1.
    ka: PU  = None
 
    # Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.2.
    ta: Seconds  = None
 
    # Regulator proportional gain (K<sub>P</sub>).  Typical Value = 20.
    kp: PU  = None
 
    # Regulator integral gain (K<sub>I</sub>).  Typical Value = 20.
    ki: PU  = None
 
    # Regulator derivative gain (K<sub>D</sub>).  Typical Value = 20.
    kd: PU  = None
 
    # Regulator derivative filter time constant(T<sub>D</sub>).  Typical Value = 0.01.
    td: Seconds  = None
 
    # Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 2.7.
    vrmax: PU  = None
 
    # Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -0.9.
    vrmin: PU  = None
 
    # Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
    # = 1.
    ke: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control
    # (T<sub>E</sub>).  Typical Value = 0.8.
    te: Seconds  = None
 
    # Excitation control system stabilizer gain (K<sub>F</sub>).  Typical Value = 0.
    kf: PU  = None
 
    # Excitation control system stabilizer time constant (T<sub>F</sub>).  Typical
    # Value = 1.
    tf: Seconds  = None
 
    # Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>).
    # Typical Value = 1.75.
    efd1: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]).  Typical Value = 0.08.
    seefd1: Simple_Float  = None
 
    # Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>).
    # Typical Value = 2.33.
    efd2: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]).  Typical Value = 0.27.
    seefd2: Simple_Float  = None
 
    # Minimum exciter voltage output(V<sub>EMIN</sub>).  Typical Value = 0.
    vemin: PU  = None
 
    # OEL input (OELin).
    # true = LV gate
    # false = subtract from error signal.
    # Typical Value = true.
    oelin: bool  = None
 
    # UEL input (UELin).
    # true = HV gate
    # false = add to error signal.
    # Typical Value = true.
    uelin: bool  = None
     