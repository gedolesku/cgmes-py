from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindPlantIEC import WindPlantIEC     

@dataclass
class WindPlantReactiveControlIEC(IdentifiedObject):
    """Simplified plant voltage and reactive power control model for use with type 3
    and type 4 wind turbine models.
    
      Reference: IEC Standard 61400-27-1 Annex E.
    """
    # Plant Q controller integral gain (<i>K</i><sub>IWPx</sub>). It is type
    # dependent parameter.
    kiwpx_: Simple_Float  = None
 
    # Plant Q controller proportional gain (<i>K</i><sub>PWPx</sub>). It is type
    # dependent parameter.
    kpwpx_: Simple_Float  = None
 
    # Plant voltage control droop (<i>K</i><sub>WPqu</sub>). It is project dependent
    # parameter.
    kwpqu_: PU  = None
 
    # Power factor control modes selector (<i>M</i><sub>WPpf</sub>). Used only if
    # mwpu is set to false.
    # true = 1: power factor control
    # false = 0: reactive power control.
    # It is project dependent parameter.
    mwppf_: bool  = None
 
    # Reactive power control modes selector (<i>M</i><sub>WPu</sub>).
    # true = 1: voltage control
    # false = 0: reactive power control.
    # It is project dependent parameter.
    mwpu_: bool  = None
 
    # Filter time constant for active power measurement (<i>T</i><sub>WPpfilt</sub>).
    # It is type dependent parameter.
    twppfilt_: Seconds  = None
 
    # Filter time constant for reactive power measurement
    # (<i>T</i><sub>WPqfilt</sub>). It is type dependent parameter.
    twpqfilt_: Seconds  = None
 
    # Filter time constant for voltage measurement (<i>T</i><sub>WPufilt</sub>). It
    # is type dependent parameter.
    twpufilt_: Seconds  = None
 
    # Lead time constant in reference value transfer function
    # (<i>T</i><sub>xft</sub>). It is type dependent parameter.
    txft_: Seconds  = None
 
    # Lag time constant in reference value transfer function (<i>T</i><sub>xfv</sub>).
    # It is type dependent parameter.
    txfv_: Seconds  = None
 
    # Voltage threshold for LVRT detection in q control (<i>u</i><sub>WPqdip</sub>).
    # It is type dependent parameter.
    uwpqdip_: PU  = None
 
    # Maximum <i>x</i><sub>WTref</sub> (<i>q</i><sub>WTref</sub> or delta
    # <i>u</i><sub>WTref</sub>) request from the plant controller
    # (<i>x</i><sub>refmax</sub>). It is project dependent parameter.
    xrefmax_: PU  = None
 
    # Minimum <i>x</i><sub>WTref</sub> (<i>q</i><sub>WTref</sub> or
    # delta<i>u</i><sub>WTref</sub>) request from the plant controller
    # (<i>x</i><sub>refmin</sub>). It is project dependent parameter.
    xrefmin_: PU  = None
 
    # Wind plant model with which this wind reactive control is associated.
    WindPlantIEC_: Optional[WindPlantIEC] = None
     