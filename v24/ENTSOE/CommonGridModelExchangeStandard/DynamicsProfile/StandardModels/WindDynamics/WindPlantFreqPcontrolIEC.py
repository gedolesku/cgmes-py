from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindPlantIEC import WindPlantIEC     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindDynamicsLookupTable import WindDynamicsLookupTable     

@dataclass
class WindPlantFreqPcontrolIEC(IdentifiedObject):
    """Frequency and active power controller model.
    
      Reference: IEC Standard 61400-27-1 Annex E.
    """
    # Maximum ramp rate of <i>p</i><sub>WTref</sub> request from the plant controller
    # to the wind turbines (<i>dp</i><sub>refmax</sub>). It is project dependent
    # parameter.
    dprefmax_: PU  = None
 
    # Minimum (negative) ramp rate of <i>p</i><sub>WTref</sub> request from the plant
    # controller to the wind turbines (<i>dp</i><sub>refmin</sub>). It is project
    # dependent parameter.
    dprefmin_: PU  = None
 
    # Plant P controller integral gain (<i>K</i><sub>IWPp</sub>). It is type
    # dependent parameter.
    kiwpp_: Simple_Float  = None
 
    # Plant P controller proportional gain (<i>K</i><sub>PWPp</sub>). It is type
    # dependent parameter.
    kpwpp_: Simple_Float  = None
 
    # Maximum <i>p</i><sub>WTref</sub> request from the plant controller to the wind
    # turbines (<i>p</i><sub>refmax</sub>). It is type dependent parameter.
    prefmax_: PU  = None
 
    # Minimum <i>p</i><sub>WTref</sub> request from the plant controller to the wind
    # turbines (<i>p</i><sub>refmin</sub>). It is type dependent parameter.
    prefmin_: PU  = None
 
    # Lead time constant in reference value transfer function
    # (<i>T</i><sub>pft</sub>). It is type dependent parameter.
    tpft_: Seconds  = None
 
    # Lag time constant in reference value transfer function (<i>T</i><sub>pfv</sub>).
    # It is type dependent parameter.
    tpfv_: Seconds  = None
 
    # Filter time constant for frequency measurement (<i>T</i><sub>WPffilt</sub>). It
    # is type dependent parameter.
    twpffilt_: Seconds  = None
 
    # Filter time constant for active power measurement (<i>T</i><sub>WPpfilt</sub>).
    # It is type dependent parameter.
    twppfilt_: Seconds  = None
 
    # Wind plant model with which this wind plant frequency and active power control
    # is associated.
    WindPlantIEC_: Optional[WindPlantIEC] = None
 
    # The frequency and active power wind plant control model with which this wind
    # dynamics lookup table is associated.
    WindDynamicsLookupTable_: List[WindDynamicsLookupTable]  = field(default_factory=list)
     