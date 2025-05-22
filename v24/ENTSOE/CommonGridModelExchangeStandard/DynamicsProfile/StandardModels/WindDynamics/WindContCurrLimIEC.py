from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindTurbineType3or4IEC import WindTurbineType3or4IEC     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindDynamicsLookupTable import WindDynamicsLookupTable     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class WindContCurrLimIEC(IdentifiedObject):
    """Current limitation model.  The current limitation model combines the physical
    limits.
    
      Reference: IEC Standard 61400-27-1 Section 6.6.5.7.
    """
    # Maximum continuous current at the wind turbine terminals
    # (<i>i</i><sub>max</sub>). It is type dependent parameter.
    imax_: PU  = None
 
    # Maximum current during voltage dip at the wind turbine terminals
    # (<i>i</i><sub>max,dip</sub>). It is project dependent parameter.
    imaxdip_: PU  = None
 
    # Limitation of type 3 stator current  (<i>M</i><sub>DFSLim</sub>):
    # - false=0: total current limitation,
    # - true=1: stator current limitation).
    # 
    # It is type dependent parameter.
    mdfslim_: bool  = None
 
    # Prioritisation of q control during LVRT (<i>M</i><sub>qpri</sub>):
    # - true = 1: reactive power priority,
    # - false = 0: active power priority.
    # 
    # It is project dependent parameter.
    mqpri_: bool  = None
 
    # Voltage measurement filter time constant (<i>T</i><sub>ufilt</sub>). It is type
    # dependent parameter.
    tufilt_: Seconds  = None
 
    # Wind turbine type 3 or 4 model with which this wind control current limitation
    # model is associated.
    WindTurbineType3or4IEC_: Optional[WindTurbineType3or4IEC] = None
 
    # The current control limitation model with which this wind dynamics lookup table
    # is associated.
    WindDynamicsLookupTable_: List[WindDynamicsLookupTable]  = field(default_factory=list)
     