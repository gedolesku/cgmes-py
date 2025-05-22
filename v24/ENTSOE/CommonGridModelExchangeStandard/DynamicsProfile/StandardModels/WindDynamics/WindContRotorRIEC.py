from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindGenTurbineType2IEC import WindGenTurbineType2IEC     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class WindContRotorRIEC(IdentifiedObject):
    """Rotor resistance control model.
    
      Reference: IEC Standard 61400-27-1 Section 6.6.5.2.
    """
    # Integral gain in rotor resistance PI controller (<i>K</i><sub>Irr</sub>). It is
    # type dependent parameter.
    kirr_: PU  = None
 
    # Filter gain for generator speed measurement (K<sub>omegafilt</sub>). It is type
    # dependent parameter.
    komegafilt_: Simple_Float  = None
 
    # Filter gain for power measurement (<i>K</i><sub>pfilt</sub>). It is type
    # dependent parameter.
    kpfilt_: Simple_Float  = None
 
    # Proportional gain in rotor resistance PI controller (<i>K</i><sub>Prr</sub>).
    # It is type dependent parameter.
    kprr_: PU  = None
 
    # Maximum rotor resistance (<i>r</i><sub>max</sub>). It is type dependent
    # parameter.
    rmax_: PU  = None
 
    # Minimum rotor resistance (<i>r</i><sub>min</sub>). It is type dependent
    # parameter.
    rmin_: PU  = None
 
    # Filter time constant for generator speed measurement
    # (<i>T</i><sub>omegafilt</sub>). It is type dependent parameter.
    tomegafilt_: Seconds  = None
 
    # Filter time constant for power measurement (<i>T</i><sub>pfilt</sub>). It is
    # type dependent parameter.
    tpfilt_: Seconds  = None
 
    # Wind turbine type 2 model with whitch this wind control rotor resistance model
    # is associated.
    WindGenTurbineType2IEC_: Optional[WindGenTurbineType2IEC] = None
     