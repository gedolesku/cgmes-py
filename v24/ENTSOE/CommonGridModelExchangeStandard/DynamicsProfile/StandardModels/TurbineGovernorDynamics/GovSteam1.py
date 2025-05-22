from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Frequency import Frequency     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovSteam1(TurbineGovernorDynamics):
    """Steam turbine governor model, based on the GovSteamIEEE1 model  (with optional
    deadband and nonlinear valve gain added).
    """
    # Base for power values (MWbase) (>0).  Unit = MW.
    mwbase: ActivePower  = None
 
    # Governor gain (reciprocal of droop) (K) (>0).  Typical Value = 25.
    k: PU  = None
 
    # Governor lag time constant (T1).  Typical Value = 0.
    t1: Seconds  = None
 
    # Governor lead time constant (T2).  Typical Value = 0.
    t2: Seconds  = None
 
    # Valve positioner time constant (T3<i>) </i>(>0).  Typical Value = 0.1.
    t3: Seconds  = None
 
    # Maximum valve opening velocity (Uo) (>0).  Unit = PU/sec.  Typical Value = 1.
    uo: Simple_Float  = None
 
    # Maximum valve closing velocity (Uc) (<0).  Unit = PU/sec.  Typical Value = -10.
    uc: Simple_Float  = None
 
    # Maximum valve opening (Pmax) (> Pmin).  Typical Value = 1.
    pmax: PU  = None
 
    # Minimum valve opening (Pmin) (>=0).  Typical Value = 0.
    pmin: PU  = None
 
    # Inlet piping/steam bowl time constant (T4).  Typical Value = 0.3.
    t4: Seconds  = None
 
    # Fraction of HP shaft power after first boiler pass (K1).  Typical Value = 0.2.
    k1: Simple_Float  = None
 
    # Fraction of LP shaft power after first boiler pass (K2).  Typical Value = 0.
    k2: Simple_Float  = None
 
    # Time constant of second boiler pass (T5).  Typical Value = 5.
    t5: Seconds  = None
 
    # Fraction of HP shaft power after second boiler pass (K3).  Typical Value = 0.3.
    k3: Simple_Float  = None
 
    # Fraction of LP shaft power after second boiler pass (K4).  Typical Value = 0.
    k4: Simple_Float  = None
 
    # Time constant of third boiler pass (T6).  Typical Value = 0.5.
    t6: Seconds  = None
 
    # Fraction of HP shaft power after third boiler pass (K5).  Typical Value = 0.5.
    k5: Simple_Float  = None
 
    # Fraction of LP shaft power after third boiler pass (K6).  Typical Value = 0.
    k6: Simple_Float  = None
 
    # Time constant of fourth boiler pass (T7).  Typical Value = 0.
    t7: Seconds  = None
 
    # Fraction of HP shaft power after fourth boiler pass (K7).  Typical Value = 0.
    k7: Simple_Float  = None
 
    # Fraction of LP shaft power after fourth boiler pass (K8).  Typical Value = 0.
    k8: Simple_Float  = None
 
    # Intentional deadband width (db1).  Unit = Hz.  Typical Value = 0.
    db1: Frequency  = None
 
    # Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
    eps: Frequency  = None
 
    # Intentional deadband indicator.
    # true = intentional deadband is applied
    # false = intentional deadband is not applied.
    # Typical Value = true.
    sdb1: bool  = None
 
    # Unintentional deadband location.
    # true = intentional deadband is applied before point "A"
    # false = intentional deadband is applied after point "A".
    # Typical Value = true.
    sdb2: bool  = None
 
    # Unintentional deadband (db2).  Unit = MW.  Typical Value = 0.
    db2: ActivePower  = None
 
    # Nonlinear valve characteristic.
    # true = nonlinear valve characteristic is used
    # false = nonlinear valve characteristic is not used.
    # Typical Value = true.
    valve: bool  = None
 
    # Nonlinear gain valve position point 1 (GV1).  Typical Value = 0.
    gv1: PU  = None
 
    # Nonlinear gain power value point 1 (Pgv1).  Typical Value = 0.
    pgv1: PU  = None
 
    # Nonlinear gain valve position point 2 (GV2).  Typical Value = 0.4.
    gv2: PU  = None
 
    # Nonlinear gain power value point 2 (Pgv2).  Typical Value = 0.75.
    pgv2: PU  = None
 
    # Nonlinear gain valve position point 3 (GV3).  Typical Value = 0.5.
    gv3: PU  = None
 
    # Nonlinear gain power value point 3 (Pgv3).  Typical Value = 0.91.
    pgv3: PU  = None
 
    # Nonlinear gain valve position point 4 (GV4).  Typical Value = 0.6.
    gv4: PU  = None
 
    # Nonlinear gain power value point 4 (Pgv4).  Typical Value = 0.98.
    pgv4: PU  = None
 
    # Nonlinear gain valve position point 5 (GV5).  Typical Value = 1.
    gv5: PU  = None
 
    # Nonlinear gain power value point 5 (Pgv5).  Typical Value = 1.
    pgv5: PU  = None
 
    # Nonlinear gain valve position point 6 (GV6).  Typical Value = 0.
    gv6: PU  = None
 
    # Nonlinear gain power value point 6 (Pgv6).  Typical Value = 0.
    pgv6: PU  = None
     