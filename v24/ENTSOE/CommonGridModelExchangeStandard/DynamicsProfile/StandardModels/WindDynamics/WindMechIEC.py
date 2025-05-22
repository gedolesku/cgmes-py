from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindTurbineType4bIEC import WindTurbineType4bIEC     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindGenTurbineType3IEC import WindGenTurbineType3IEC     

@dataclass
class WindMechIEC(IdentifiedObject):
    """Two mass model.
    
      Reference: IEC Standard 61400-27-1 Section 6.6.2.1.
    """
    # Drive train damping (<i>c</i><i><sub>drt</sub></i><i>)</i>. It is type
    # dependent parameter.
    cdrt: PU  = None
 
    # Inertia constant of generator (<i>H</i><sub>gen</sub>). It is type dependent
    # parameter.
    hgen: Seconds  = None
 
    # Inertia constant of wind turbine rotor (<i>H</i><sub>WTR</sub>). It is type
    # dependent parameter.
    hwtr: Seconds  = None
 
    # Drive train stiffness (<i>k</i><i><sub>drt</sub></i>). It is type dependent
    # parameter.
    kdrt: PU  = None
 
    # Wind turbine type 4B model with which this wind mechanical model is associated.
    WindTurbineType4bIEC_ref: Optional[WindTurbineType4bIEC] = None
    WindTurbineType4bIEC: str = None
 
    # Wind turbine Type 3 model with which this wind mechanical model is associated.
    WindGenTurbineType3IEC_ref: Optional[WindGenTurbineType3IEC] = None
    WindGenTurbineType3IEC: str = None
     