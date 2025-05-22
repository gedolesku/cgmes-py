from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
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
    kirr: PU  = None
 
    # Filter gain for generator speed measurement (K<sub>omegafilt</sub>). It is type
    # dependent parameter.
    komegafilt: Simple_Float  = None
 
    # Filter gain for power measurement (<i>K</i><sub>pfilt</sub>). It is type
    # dependent parameter.
    kpfilt: Simple_Float  = None
 
    # Proportional gain in rotor resistance PI controller (<i>K</i><sub>Prr</sub>).
    # It is type dependent parameter.
    kprr: PU  = None
 
    # Maximum rotor resistance (<i>r</i><sub>max</sub>). It is type dependent
    # parameter.
    rmax: PU  = None
 
    # Minimum rotor resistance (<i>r</i><sub>min</sub>). It is type dependent
    # parameter.
    rmin: PU  = None
 
    # Filter time constant for generator speed measurement
    # (<i>T</i><sub>omegafilt</sub>). It is type dependent parameter.
    tomegafilt: Seconds  = None
 
    # Filter time constant for power measurement (<i>T</i><sub>pfilt</sub>). It is
    # type dependent parameter.
    tpfilt: Seconds  = None
 
    # Wind turbine type 2 model with whitch this wind control rotor resistance model
    # is associated.
    WindGenTurbineType2IEC_ref: Optional[WindGenTurbineType2IEC] = None
    WindGenTurbineType2IEC: str = None
     