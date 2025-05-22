from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindLVRTQcontrolModesKind import WindLVRTQcontrolModesKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindQcontrolModesKind import WindQcontrolModesKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindTurbineType3or4IEC import WindTurbineType3or4IEC     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class WindContQIEC(IdentifiedObject):
    """Q control model.
    
      Reference: IEC Standard 61400-27-1 Section 6.6.5.6.
    """
    # Maximum reactive current injection during dip (i<sub>qh1</sub>). It is type
    # dependent parameter.
    iqh1_: PU  = None
 
    # Maximum reactive current injection (i<sub>qmax</sub>). It is type dependent
    # parameter.
    iqmax_: PU  = None
 
    # Minimum reactive current injection (i<sub>qmin</sub>). It is type dependent
    # parameter.
    iqmin_: PU  = None
 
    # Post fault reactive current injection (<i>i</i><sub>qpost</sub>). It is project
    # dependent parameter.
    iqpost_: PU  = None
 
    # Reactive power PI controller integration gain (<i>K</i><sub>I,q</sub>). It is
    # type dependent parameter.
    kiq_: PU  = None
 
    # Voltage PI controller integration gain (<i>K</i><sub>I,u</sub>). It is type
    # dependent parameter.
    kiu_: PU  = None
 
    # Reactive power PI controller proportional gain (<i>K</i><sub>P,q</sub>). It is
    # type dependent parameter.
    kpq_: PU  = None
 
    # Voltage PI controller proportional gain (<i>K</i><sub>P,u</sub>). It is type
    # dependent parameter.
    kpu_: PU  = None
 
    # Voltage scaling factor for LVRT current (<i>K</i><sub>qv</sub>). It is project
    # dependent parameter.
    kqv_: PU  = None
 
    # Maximum reactive power (q<sub>max</sub>). It is type dependent parameter.
    qmax_: PU  = None
 
    # Minimum reactive power (q<sub>min</sub>). It is type dependent parameter.
    qmin_: PU  = None
 
    # Resistive component of voltage drop impedance (<i>r</i><sub>droop</sub>). It is
    # project dependent parameter.
    rdroop_: PU  = None
 
    # Time constant in reactive current lag (T<sub>iq</sub>). It is type dependent
    # parameter.
    tiq_: Seconds  = None
 
    # Power measurement filter time constant (<i>T</i><sub>pfilt</sub>). It is type
    # dependent parameter.
    tpfilt_: Seconds  = None
 
    # Length of time period where post fault reactive power is injected
    # (<i>T</i><sub>post</sub>). It is project dependent parameter.
    tpost_: Seconds  = None
 
    # Time constant in reactive power order lag (<i>T</i><sub>qord</sub>). It is type
    # dependent parameter.
    tqord_: Seconds  = None
 
    # Voltage measurement filter time constant (<i>T</i><sub>ufilt</sub>). It is type
    # dependent parameter.
    tufilt_: Seconds  = None
 
    # Voltage dead band lower limit (<i>u</i><sub>db1</sub>). It is type dependent
    # parameter.
    udb1_: PU  = None
 
    # Voltage dead band upper limit (<i>u</i><sub>db2</sub>). It is type dependent
    # parameter.
    udb2_: PU  = None
 
    # Maximum voltage in voltage PI controller integral term (u<sub>max</sub>). It is
    # type dependent parameter.
    umax_: PU  = None
 
    # Minimum voltage in voltage PI controller integral term (u<sub>min</sub>). It is
    # type dependent parameter.
    umin_: PU  = None
 
    # Voltage threshold for LVRT detection in q control (<i>u</i><sub>qdip</sub>). It
    # is type dependent parameter.
    uqdip_: PU  = None
 
    # User defined bias in voltage reference (<i>u</i><sub>ref0</sub>), used when
    # <i>M</i><sub>qG</sub> =<i> M</i><sub>G,u</sub>. It is case dependent parameter.
    uref0_: PU  = None
 
    # Types of LVRT Q control modes (<i>M</i><sub>qLVRT</sub>). It is project
    # dependent parameter.
    windLVRTQcontrolModesType_: WindLVRTQcontrolModesKind  = None
 
    # Types of general wind turbine Q control modes (<i>M</i><sub>qG</sub>).  It is
    # project dependent parameter.
    windQcontrolModesType_: WindQcontrolModesKind  = None
 
    # Inductive component of voltage drop impedance (<i>x</i><sub>droop</sub>). It is
    # project dependent parameter.
    xdroop_: PU  = None
 
    # Wind turbine type 3 or 4 model with which this reactive control mode is
    # associated.
    WindTurbineType3or4IEC_: Optional[WindTurbineType3or4IEC] = None
     