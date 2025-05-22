from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindGenTurbineType3IEC import WindGenTurbineType3IEC     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindDynamicsLookupTable import WindDynamicsLookupTable     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class WindContPType3IEC(IdentifiedObject):
    """P control model Type 3.
    
      Reference: IEC Standard 61400-27-1 Section 6.6.5.3.
    """
    # Maximum wind turbine power ramp rate (<i>dp</i><sub>max</sub>). It is project
    # dependent parameter.
    dpmax_: PU  = None
 
    # Limitation of torque rise rate during LVRT for S<sub>1</sub>
    # (d<i>T</i><sub>risemaxLVRT</sub>). It is project dependent parameter.
    dtrisemaxlvrt_: PU  = None
 
    # Gain for active drive train damping (<i>K</i><sub>DTD</sub>). It is type
    # dependent parameter.
    kdtd_: PU  = None
 
    # PI controller integration parameter (<i>K</i><sub>Ip</sub>). It is type
    # dependent parameter.
    kip_: PU  = None
 
    # PI controller proportional gain (<i>K</i><sub>Pp</sub>). It is type dependent
    # parameter.
    kpp_: PU  = None
 
    # Enable LVRT power control mode (M<sub>pLVRT).</sub>
    # true = 1: voltage control
    # false = 0: reactive power control.
    # 
    # It is project dependent parameter.
    mplvrt_: bool  = None
 
    # Offset to reference value that limits controller action during rotor speed
    # changes (omega<sub>offset</sub>). It is case dependent parameter.
    omegaoffset_: PU  = None
 
    # Maximum active drive train damping power (<i>p</i><sub>DTDmax</sub>). It is
    # type dependent parameter.
    pdtdmax_: PU  = None
 
    # Ramp limitation of torque, required in some grid codes
    # (<i>R</i><sub>ramp</sub>). It is project dependent parameter.
    rramp_: PU  = None
 
    # Time<sub> </sub>delay after deep voltage sags (T<sub>DVS</sub>). It is project
    # dependent parameter.
    tdvs_: Seconds  = None
 
    # Minimum electrical generator torque (<i>T</i><sub>emin</sub>). It is type
    # dependent parameter.
    temin_: PU  = None
 
    # Filter time constant for generator speed measurement
    # (<i>T</i><sub>omegafilt</sub>). It is type dependent parameter.
    tomegafilt_: Seconds  = None
 
    # Filter time constant for power measurement (<i>T</i><sub>pfilt</sub>). It is
    # type dependent parameter.
    tpfilt_: Seconds  = None
 
    # Time constant in power order lag (<i>T</i><sub>pord</sub>). It is type
    # dependent parameter.
    tpord_: PU  = None
 
    # Filter time constant for voltage measurement (<i>T</i><sub>ufilt</sub>). It is
    # type dependent parameter.
    tufilt_: Seconds  = None
 
    # Voltage scaling factor of reset-torque (T<sub>uscale</sub>). It is project
    # dependent parameter.
    tuscale_: PU  = None
 
    # Time constant in speed reference filter (<i>T</i><sub>omega,ref</sub>). It is
    # type dependent parameter.
    twref_: Seconds  = None
 
    # Voltage limit for hold LVRT status after deep voltage sags
    # (<i>u</i><i><sub>DVS</sub></i>). It is project dependent parameter.
    udvs_: PU  = None
 
    # Voltage dip threshold for P-control (<i>u</i><sub>Pdip</sub>).  Part of turbine
    # control, often different (e.g 0.8) from converter thresholds. It is project
    # dependent parameter.
    updip_: PU  = None
 
    # Active drive train damping frequency (omega<sub>DTD</sub>). It can be
    # calculated from two mass model parameters. It is type dependent parameter.
    wdtd_: PU  = None
 
    # Coefficient for active drive train damping (zeta). It is type dependent
    # parameter.
    zeta_: Simple_Float  = None
 
    # Wind turbine type 3 model with which this Wind control P type 3 model is
    # associated.
    WindGenTurbineType3IEC_: Optional[WindGenTurbineType3IEC] = None
 
    # The P control type 3 model with which this wind dynamics lookup table is
    # associated.
    WindDynamicsLookupTable_: Optional[WindDynamicsLookupTable] = None
     