from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindTurbineType3or4IEC import WindTurbineType3or4IEC     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindTurbineType1or2IEC import WindTurbineType1or2IEC     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class WindProtectionIEC(IdentifiedObject):
    """The grid protection model includes protection against over and under voltage,
    and against over and under frequency.
    
      Reference: IEC Standard 614000-27-1 Section 6.6.6.
    """
    # Set of wind turbine over frequency protection levels
    # (<i>f</i><i><sub>over</sub></i>). It is project dependent parameter. 
    fover: PU  = None
 
    # Set of wind turbine under frequency protection levels
    # (<i>f</i><i><sub>under</sub></i>). It is project dependent parameter.
    funder: PU  = None
 
    # Set of corresponding wind turbine over frequency protection disconnection times
    # (<i>T</i><i><sub>fover</sub></i>). It is project dependent parameter.
    tfover: Seconds  = None
 
    # Set of corresponding wind turbine under frequency protection disconnection
    # times (<i>T</i><i><sub>funder</sub></i>). It is project dependent parameter.
    tfunder: Seconds  = None
 
    # Set of corresponding wind turbine over voltage protection disconnection times
    # (<i>T</i><i><sub>uover</sub></i>). It is project dependent parameter.
    tuover: Seconds  = None
 
    # Set of corresponding wind turbine under voltage protection disconnection times
    # (<i>T</i><i><sub>uunder</sub></i>). It is project dependent parameter.
    tuunder: Seconds  = None
 
    # Set of wind turbine over voltage protection levels
    # (<i>u</i><i><sub>over</sub></i>). It is project dependent parameter.
    uover: PU  = None
 
    # Set of wind turbine under voltage protection levels
    # (<i>u</i><i><sub>under</sub></i>). It is project dependent parameter.
    uunder: PU  = None
 
    # Wind generator type 3 or 4 model with which this wind turbine protection model
    # is associated.
    WindTurbineType3or4IEC_ref: Optional[WindTurbineType3or4IEC] = None
    WindTurbineType3or4IEC: str = None
 
    # Wind generator type 1 or 2 model with which this wind turbine protection model
    # is associated.
    WindTurbineType1or2IEC_ref: Optional[WindTurbineType1or2IEC] = None
    WindTurbineType1or2IEC: str = None
     