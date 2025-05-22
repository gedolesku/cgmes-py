from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindGenTurbineType2IEC import WindGenTurbineType2IEC     

@dataclass
class WindPitchContEmulIEC(IdentifiedObject):
    """Pitch control emulator model.
    
      Reference: IEC Standard 61400-27-1 Section 6.6.5.1.
    """
    # Power error gain (<i>K</i><sub>droop</sub>). It is case dependent parameter.
    kdroop_: Simple_Float  = None
 
    # Pitch control emulator integral constant (<i>K</i><sub>I,pce</sub>). It is type
    # dependent parameter.
    kipce_: Simple_Float  = None
 
    # Aerodynamic power change vs. omega<sub>WTR </sub>change
    # (<i>K</i><sub>omegaaero</sub>). It is case dependent parameter.
    komegaaero_: PU  = None
 
    # Pitch control emulator proportional constant (<i>K</i><sub>P,pce</sub>). It is
    # type dependent parameter.
    kppce_: Simple_Float  = None
 
    # Rotor speed in initial steady state (omega<sub>ref</sub>). It is case dependent
    # parameter.
    omegaref_: PU  = None
 
    # Maximum steady state power (<i>p</i><sub>imax</sub>). It is case dependent
    # parameter.
    pimax_: PU  = None
 
    # Minimum steady state power (<i>p</i><sub>imin</sub>). It is case dependent
    # parameter.
    pimin_: PU  = None
 
    # First time constant in pitch control lag (<i>T</i><sub>1</sub>). It is type
    # dependent parameter.
    t1_: Seconds  = None
 
    # Second time constant in pitch control lag (<i>T</i><sub>2</sub>). It is type
    # dependent parameter.
    t2_: Seconds  = None
 
    # Time constant in generator air gap power lag (<i>T</i><sub>pe</sub>). It is
    # type dependent parameter.
    tpe_: Seconds  = None
 
    # Wind turbine type 2 model with which this Pitch control emulator model is
    # associated.
    WindGenTurbineType2IEC_: Optional[WindGenTurbineType2IEC] = None
     