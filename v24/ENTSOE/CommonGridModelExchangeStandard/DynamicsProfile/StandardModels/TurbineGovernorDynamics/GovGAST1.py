from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Frequency import Frequency     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovGAST1(TurbineGovernorDynamics):
    """Modified single shaft gas turbine.
    """
    # Base for power values (MWbase) (> 0).  Unit = MW.
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
    # shaft engine, or with the compressibility of gas in the plenum of the free
    # power turbine of an aero-derivative unit, for example.  Typical Value = 0.5.
    t2_: Seconds  = None
 
    # Turbine exhaust temperature time constant (T3).  T3 represents delay in the
    # exhaust temperature and load limiting system. Typical Value = 3.
    t3_: Seconds  = None
 
    # Ambient temperature load limit (Lmax).  Lmax is the turbine power output
    # corresponding to the limiting exhaust gas temperature.  Typical Value = 1.
    lmax_: PU  = None
 
    # Temperature limiter gain (Kt).  Typical Value = 3.
    kt_: PU  = None
 
    # Maximum turbine power, PU of MWbase (Vmax).  Typical Value = 1.
    vmax_: PU  = None
 
    # Minimum turbine power, PU of MWbase (Vmin).  Typical Value = 0.
    vmin_: PU  = None
 
    # Fuel flow at zero power output (Fidle).  Typical Value = 0.18.
    fidle_: PU  = None
 
    # Maximum fuel valve opening rate (Rmax).  Unit = PU/sec.  Typical Value = 1.
    rmax_: Simple_Float  = None
 
    # Valve position change allowed at fast rate (Loadinc).  Typical Value = 0.05.
    loadinc_: PU  = None
 
    # Valve position averaging time constant (Tltr).  Typical Value = 10.
    tltr_: Seconds  = None
 
    # Maximum long term fuel valve opening rate (Ltrate).  Typical Value = 0.02.
    ltrate_: Simple_Float  = None
 
    # Turbine power time constant numerator scale factor (a).  Typical Value = 0.8.
    a_: Simple_Float  = None
 
    # Turbine power time constant denominator scale factor (b).  Typical Value = 1.
    b_: Simple_Float  = None
 
    # Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0.
    db1_: Frequency  = None
 
    # Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
    eps_: Frequency  = None
 
    # Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0.
    db2_: ActivePower  = None
 
    # Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0.
    gv1_: PU  = None
 
    # Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0.
    pgv1_: PU  = None
 
    # Nonlinear gain point 2,PU gv (Gv2).  Typical Value = 0.
    gv2_: PU  = None
 
    # Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0.
    pgv2_: PU  = None
 
    # Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0.
    gv3_: PU  = None
 
    # Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0.
    pgv3_: PU  = None
 
    # Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0.
    gv4_: PU  = None
 
    # Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0.
    pgv4_: PU  = None
 
    # Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0.
    gv5_: PU  = None
 
    # Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.
    pgv5_: PU  = None
 
    # Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0.
    gv6_: PU  = None
 
    # Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0.
    pgv6_: PU  = None
 
    # Governor gain (Ka).  Typical Value = 0.
    ka_: PU  = None
 
    # Governor lead time constant (T4).  Typical Value = 0.
    t4_: Seconds  = None
 
    # Governor lag time constant (T5).  Typical Value = 0.
    t5_: Seconds  = None
     