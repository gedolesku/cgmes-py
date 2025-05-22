from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.LoadDynamics.GenericNonLinearLoadModelKind import GenericNonLinearLoadModelKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.LoadDynamics.LoadDynamics import LoadDynamics

@dataclass
class LoadGenericNonLinear(LoadDynamics):
    """These load models (known also as generic non-linear dynamic (GNLD) load models)
    can be used in mid-term and long-term voltage stability simulations (i.e., to
    study voltage collapse), as they can replace a more detailed representation of
    aggregate load, including induction motors, thermostatically controlled and
    static loads.
    """
    # Type of generic non-linear load model.
    genericNonLinearLoadModelType_: GenericNonLinearLoadModelKind  = None
 
    # Dynamic portion of active load (P<sub>T</sub>).
    pt_: Simple_Float  = None
 
    # Dynamic portion of reactive load (Q<sub>T</sub>).
    qt_: Simple_Float  = None
 
    # Time constant of lag function of active power (T<sub>P</sub>).
    tp_: Seconds  = None
 
    # Time constant of lag function of reactive power (T<sub>Q</sub>).
    tq_: Seconds  = None
 
    # Steady state voltage index for active power (LS).
    ls_: Simple_Float  = None
 
    # Transient voltage index for active power (LT).
    lt_: Simple_Float  = None
 
    # Steady state voltage index for reactive power (BS).
    bs_: Simple_Float  = None
 
    # Transient voltage index for reactive power (BT).
    bt_: Simple_Float  = None
     