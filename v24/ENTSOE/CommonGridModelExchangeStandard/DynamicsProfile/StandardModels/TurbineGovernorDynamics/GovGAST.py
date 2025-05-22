from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovGAST(TurbineGovernorDynamics):
    """Single shaft gas turbine.
    """
    # Base for power values (MWbase) (> 0).
    mwbase_: ActivePower  = None
 
    # Permanent droop (R).  Typical Value = 0.04.
    r_: PU  = None
 
    # Governor mechanism time constant (T1).  T1 represents the natural valve
    # positioning time constant of the governor for small disturbances, as seen when
    # rate limiting is not in effect.  Typical Value = 0.5.
    t1_: Seconds  = None
 
    # Turbine power time constant (T2).  T2 represents delay due to internal energy
    # storage of the gas turbine engine. T2 can be used to give a rough approximation
    # to the delay associated with acceleration of the compressor spool of a multi-
    # shaft engine, or with the compressibility of gas in the plenum of a the free
    # power turbine of an aero-derivative unit, for example.  Typical Value = 0.5.
    t2_: Seconds  = None
 
    # Turbine exhaust temperature time constant (T3).  Typical Value = 3.
    t3_: Seconds  = None
 
    # Ambient temperature load limit (Load Limit).  Typical Value = 1.
    at_: PU  = None
 
    # Temperature limiter gain (Kt).  Typical Value = 3.
    kt_: PU  = None
 
    # Maximum turbine power, PU of MWbase (Vmax).  Typical Value = 1.
    vmax_: PU  = None
 
    # Minimum turbine power, PU of MWbase (Vmin).  Typical Value = 0.
    vmin_: PU  = None
 
    # Turbine damping factor (Dturb).  Typical Value = 0.18.
    dturb_: PU  = None
     