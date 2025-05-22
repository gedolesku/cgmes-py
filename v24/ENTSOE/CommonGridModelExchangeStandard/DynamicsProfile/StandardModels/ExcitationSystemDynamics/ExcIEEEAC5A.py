from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEAC5A(ExcitationSystemDynamics):
    """The class represents IEEE Std 421.5-2005 type AC5A model. The model represents
    a simplified model for brushless excitation systems. The regulator is supplied
    from a source, such as a permanent magnet generator, which is not affected by
    system disturbances.  Unlike other ac models, this model uses loaded rather
    than open circuit exciter saturation data in the same way as it is used for the
    dc models.  Because the model has been widely implemented by the industry, it
    is sometimes used to represent other types of systems when either detailed data
    for them are not available or simplified models are required.
    
    
      Reference: IEEE Standard 421.5-2005 Section 6.5.
    """
    # Voltage regulator gain (K<sub>A</sub>).  Typical Value = 400.
    ka: PU  = None
 
    # Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.02.
    ta: Seconds  = None
 
    # Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 7.3.
    vrmax: PU  = None
 
    # Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -7.3.
    vrmin: PU  = None
 
    # Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
    # = 1.
    ke: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control
    # (T<sub>E</sub>).  Typical Value = 0.8.
    te: Seconds  = None
 
    # Excitation control system stabilizer gains (K<sub>F</sub>).  Typical Value = 0.
    # 03.
    kf: PU  = None
 
    # Excitation control system stabilizer time constant (T<sub>F1</sub>).  Typical
    # Value = 1.
    tf1: Seconds  = None
 
    # Excitation control system stabilizer time constant (T<sub>F2</sub>).  Typical
    # Value = 1.
    tf2: Seconds  = None
 
    # Excitation control system stabilizer time constant (T<sub>F3</sub>).  Typical
    # Value = 1.
    tf3: Seconds  = None
 
    # Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>).
    # Typical Value = 5.6.
    efd1: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]).  Typical Value = 0.86.
    seefd1: Simple_Float  = None
 
    # Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>).
    # Typical Value = 4.2.
    efd2: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]).  Typical Value = 0.5.
    seefd2: Simple_Float  = None
     