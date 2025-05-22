from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.AngleDegrees import AngleDegrees     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindGenTurbineType3IEC import WindGenTurbineType3IEC     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class WindContPitchAngleIEC(IdentifiedObject):
    """Pitch angle control model.
    
      Reference: IEC Standard 61400-27-1 Section 6.6.5.8.
    """
    # Maximum pitch positive ramp rate (d<i>theta</i><sub>max</sub>). It is type
    # dependent parameter. Unit = degrees/sec. 
    dthetamax: Simple_Float  = None
 
    # Maximum pitch negative ramp rate (d<i>theta</i><sub>min</sub>). It is type
    # dependent parameter. Unit = degrees/sec. 
    dthetamin: Simple_Float  = None
 
    # Power PI controller integration gain (<i>K</i><sub>Ic</sub>). It is type
    # dependent parameter.
    kic: PU  = None
 
    # Speed PI controller integration gain (<i>K</i><sub>Iomega</sub>). It is type
    # dependent parameter.
    kiomega: PU  = None
 
    # Power PI controller proportional gain (<i>K</i><sub>Pc</sub>). It is type
    # dependent parameter.
    kpc: PU  = None
 
    # Speed PI controller proportional gain (<i>K</i><sub>Pomega</sub>). It is type
    # dependent parameter.
    kpomega: PU  = None
 
    # Pitch cross coupling gain (K<sub>PX</sub>). It is type dependent parameter.
    kpx: PU  = None
 
    # Maximum pitch angle (<i>theta</i><sub>max</sub>). It is type dependent
    # parameter.
    thetamax: AngleDegrees  = None
 
    # Minimum pitch angle (<i>theta</i><sub>min</sub>). It is type dependent
    # parameter.
    thetamin: AngleDegrees  = None
 
    # Pitch time constant (t<i>theta</i>). It is type dependent parameter.
    ttheta: Seconds  = None
 
    # Wind turbine type 3 model with which this pitch control model is associated.
    WindGenTurbineType3IEC_ref: Optional[WindGenTurbineType3IEC] = None
    WindGenTurbineType3IEC: str = None
     