from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindMechIEC import WindMechIEC     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindTurbineType3or4IEC import WindTurbineType3or4IEC
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindContPitchAngleIEC import WindContPitchAngleIEC     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindContPType3IEC import WindContPType3IEC     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindAeroLinearIEC import WindAeroLinearIEC     

@dataclass
class WindGenTurbineType3IEC(WindTurbineType3or4IEC):
    """Generator model for wind turbines of IEC type 3A and 3B.
    """
    # Maximum active current ramp rate (di<sub>pmax</sub>). It is project dependent
    # parameter.
    dipmax: PU  = None
 
    # Maximum reactive current ramp rate (di<sub>qmax</sub>). It is project dependent
    # parameter.
    diqmax: PU  = None
 
    # Wind mechanical model associated with this wind turbine Type 3 model.
    WindMechIEC_ref: Optional[WindMechIEC] = None
    WindMechIEC: str = None
 
    # Wind control pitch angle model associated with this wind turbine type 3.
    WindContPitchAngleIEC_ref: Optional[WindContPitchAngleIEC] = None
    WindContPitchAngleIEC: str = None
 
    # Wind control P type 3 model associated with this wind turbine type 3 model.
    WindContPType3IEC_ref: Optional[WindContPType3IEC] = None
    WindContPType3IEC: str = None
 
    # Wind aerodynamic model associated with this wind generator type 3 model.
    WindAeroLinearIEC_ref: Optional[WindAeroLinearIEC] = None
    WindAeroLinearIEC: str = None
     