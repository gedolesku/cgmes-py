from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Temperature import Temperature     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovGASTWD(TurbineGovernorDynamics):
    """Woodward Gas turbine governor model.
    """
    # Base for power values (MWbase) (> 0).  Unit = MW.
    mwbase_: ActivePower  = None
 
    # (Kdroop).
    kdroop_: PU  = None
 
    # PID Proportional gain (Kp).
    kp_: PU  = None
 
    # Isochronous Governor Gain (Ki).
    ki_: PU  = None
 
    # Drop Governor Gain (Kd).
    kd_: PU  = None
 
    # Turbine and exhaust delay (Etd).
    etd_: Seconds  = None
 
    # Compressor discharge time constant (Tcd).
    tcd_: Seconds  = None
 
    # Turbine rating (Trate).  Unit = MW.
    trate_: ActivePower  = None
 
    # Fuel Control Time Constant (T).
    t_: Seconds  = None
 
    # Maximum Turbine limit (Tmax).
    tmax_: PU  = None
 
    # Minimum Turbine limit (Tmin).
    tmin_: PU  = None
 
    # Combustion reaction time delay (Ecr).
    ecr_: Seconds  = None
 
    # Ratio of Fuel Adjustment (K3).
    k3_: PU  = None
 
    # Valve positioner (<i>A</i>).
    a_: Simple_Float  = None
 
    # Valve positioner (<i>B</i>). 
    b_: Simple_Float  = None
 
    # Valve positioner (<i>C</i>). 
    c_: Simple_Float  = None
 
    # Fuel system time constant (Tf).
    tf_: Seconds  = None
 
    # Fuel system feedback (Kf).
    kf_: PU  = None
 
    # Gain of radiation shield (K5).
    k5_: PU  = None
 
    # Gain of radiation shield (K4).
    k4_: PU  = None
 
    # Radiation shield time constant (T3).
    t3_: Seconds  = None
 
    # Thermocouple time constant (T4).
    t4_: Seconds  = None
 
    # Temperature controller integration rate (Tt).
    tt_: Seconds  = None
 
    # Temperature control time constant (T5).
    t5_: Seconds  = None
 
    # Exhaust temperature Parameter (Af1).
    af1_: PU  = None
 
    # (Bf1).  Bf1 = E(1-w) where E (speed sensitivity coefficient) is 0.55 to 0.65 x
    # Tr.
    bf1_: PU  = None
 
    # Coefficient equal to 0.5(1-speed) (Af2).
    af2_: PU  = None
 
    # Turbine Torque Coefficient K<sub>hhv</sub> (depends on heating value of fuel
    # stream in combustion chamber) (Bf2).
    bf2_: PU  = None
 
    # Coefficient defining fuel flow where power output is 0% (Cf2).  Synchronous but
    # no output.  Typically 0.23 x K<sub>hhv </sub>(23% fuel flow).
    cf2_: PU  = None
 
    # Rated temperature (Tr).
    tr_: Temperature  = None
 
    # Minimum fuel flow (K6). 
    k6_: PU  = None
 
    # Temperature control (Tc).
    tc_: Temperature  = None
 
    # Power transducer time constant (Td).
    td_: Seconds  = None
     