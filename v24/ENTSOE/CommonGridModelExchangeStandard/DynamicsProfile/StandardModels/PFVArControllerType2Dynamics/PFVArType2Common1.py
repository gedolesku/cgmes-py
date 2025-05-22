from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PFVArControllerType2Dynamics.PFVArControllerType2Dynamics import PFVArControllerType2Dynamics

@dataclass
class PFVArType2Common1(PFVArControllerType2Dynamics):
    """Power factor / Reactive power regulator. This model represents the power factor
    or reactive power controller such as the Basler SCP-250. The controller
    measures power factor or reactive power (PU on generator rated power) and
    compares it with the operator's set point.
    """
    # Selector (J).
    # true = control mode for reactive power
    # false = control mode for power factor.
    j_: bool  = None
 
    # Proportional gain (Kp).
    kp_: PU  = None
 
    # Reset gain (Ki).
    ki_: PU  = None
 
    # Output limit (max).
    max_: PU  = None
 
    # Reference value of reactive power or power factor (Ref).
    # The reference value is initialised by this model. This initialisation may
    # override the value exchanged by this attribute to represent a plant operator's
    # change of the reference setting.
    ref_: PU  = None
     