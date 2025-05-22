from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.AngleDegrees import AngleDegrees     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindGenTurbineType3IEC import WindGenTurbineType3IEC     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class WindAeroLinearIEC(IdentifiedObject):
    """The linearised aerodynamic model.
    
      Reference: IEC Standard 614000-27-1 Section 6.6.1.2.
    """
    # Partial derivative of aerodynamic power with respect to changes in WTR speed
    # (<i>dp</i><i><sub>omega</sub></i>). It is case dependent parameter.
    dpomega_: PU  = None
 
    # Partial derivative of aerodynamic power with respect to changes in pitch angle
    # (<i>dp</i><i><sub>theta</sub></i>). It is case dependent parameter.
    dptheta_: PU  = None
 
    # Rotor speed if the wind turbine is not derated
    # (<i>omega</i><i><sub>0</sub></i>). It is case dependent parameter.
    omegazero_: PU  = None
 
    # Available aerodynamic power (<i>p</i><sub>avail</sub>). It is case dependent
    # parameter.
    pavail_: PU  = None
 
    # Pitch angle if the wind turbine is not derated
    # (<i>theta</i><i><sub>0</sub></i>). It is case dependent parameter.
    thetazero_: AngleDegrees  = None
 
    # Wind generator type 3 model with which this wind aerodynamic model is
    # associated.
    WindGenTurbineType3IEC_: Optional[WindGenTurbineType3IEC] = None
     