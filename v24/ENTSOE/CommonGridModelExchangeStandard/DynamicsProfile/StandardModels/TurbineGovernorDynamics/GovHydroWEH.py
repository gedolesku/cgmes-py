from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovHydroWEH(TurbineGovernorDynamics):
    """Woodward Electric Hydro Governor Model.
    """
    # Base for power values (MWbase) (>0).  Unit = MW.
    mwbase_: ActivePower  = None
 
    # Permanent droop for governor output feedback (R-Perm-Gate).
    rpg_: Simple_Float  = None
 
    # Permanent droop for electrical power feedback (R-Perm-Pe).
    rpp_: Simple_Float  = None
 
    # Electrical power droop time constant (Tpe).
    tpe_: Seconds  = None
 
    # Derivative control gain (Kp).
    kp_: PU  = None
 
    # Derivative controller Integral gain (Ki).
    ki_: PU  = None
 
    # Derivative controller derivative gain (Kd).
    kd_: PU  = None
 
    # Derivative controller time constant to limit the derivative characteristic
    # beyond a breakdown frequency to avoid amplification of high-frequency noise
    # (Td).
    td_: Seconds  = None
 
    # Pilot Valve time lag time constant (Tp).
    tp_: Seconds  = None
 
    # Distributive Valve time lag time constant (Tdv).
    tdv_: Seconds  = None
 
    # Value to allow the Distribution valve controller to advance beyond the gate
    # movement rate limit (Tg).
    tg_: Seconds  = None
 
    # Maximum gate opening rate (Gtmxop).
    gtmxop_: PU  = None
 
    # Maximum gate closing rate (Gtmxcl).
    gtmxcl_: PU  = None
 
    # Maximum Gate Position (Gmax).
    gmax_: PU  = None
 
    # Minimum Gate Position (Gmin).
    gmin_: PU  = None
 
    # Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed
    # (PU).
    dturb_: PU  = None
 
    # Water inertia time constant (Tw) (>0).
    tw_: Seconds  = None
 
    # Speed Dead Band (db).
    db_: PU  = None
 
    # Value to allow the Pilot valve controller to advance beyond the gate limits
    # (Dpv).
    dpv_: PU  = None
 
    # Value to allow the integral controller to advance beyond the gate limits (Dicn).
    dicn_: PU  = None
 
    # Feedback signal selection (Sw).
    # true = PID Output (if R-Perm-Gate=droop and R-Perm-Pe=0)
    # false = Electrical Power (if R-Perm-Gate=0 and R-Perm-Pe=droop) or
    # false = Gate Position (if R-Perm-Gate=droop and R-Perm-Pe=0).
    feedbackSignal_: bool  = None
 
    # Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing
    # water flow through the turbine as a function of gate position to produce steady
    # state flow.
    gv1_: PU  = None
 
    # Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing
    # water flow through the turbine as a function of gate position to produce steady
    # state flow.
    gv2_: PU  = None
 
    # Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing
    # water flow through the turbine as a function of gate position to produce steady
    # state flow.
    gv3_: PU  = None
 
    # Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing
    # water flow through the turbine as a function of gate position to produce steady
    # state flow.
    gv4_: PU  = None
 
    # Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing
    # water flow through the turbine as a function of gate position to produce steady
    # state flow.
    gv5_: PU  = None
 
    # Flow Gate 1 (Fl1).  Flow value for gate position point 1 for lookup table
    # representing water flow through the turbine as a function of gate position to
    # produce steady state flow.
    fl1_: PU  = None
 
    # Flow Gate 2 (Fl2).  Flow value for gate position point 2 for lookup table
    # representing water flow through the turbine as a function of gate position to
    # produce steady state flow.
    fl2_: PU  = None
 
    # Flow Gate 3 (Fl3).  Flow value for gate position point 3 for lookup table
    # representing water flow through the turbine as a function of gate position to
    # produce steady state flow.
    fl3_: PU  = None
 
    # Flow Gate 4 (Fl4).  Flow value for gate position point 4 for lookup table
    # representing water flow through the turbine as a function of gate position to
    # produce steady state flow.
    fl4_: PU  = None
 
    # Flow Gate 5 (Fl5).  Flow value for gate position point 5 for lookup table
    # representing water flow through the turbine as a function of gate position to
    # produce steady state flow.
    fl5_: PU  = None
 
    # Flow P1 (Fp1).  Turbine Flow value for point 1 for lookup table representing
    # per unit mechanical power on machine MVA rating as a function of turbine flow.
    fp1_: PU  = None
 
    # Flow P2 (Fp2).  Turbine Flow value for point 2 for lookup table representing
    # per unit mechanical power on machine MVA rating as a function of turbine flow.
    fp2_: PU  = None
 
    # Flow P3 (Fp3).  Turbine Flow value for point 3 for lookup table representing
    # per unit mechanical power on machine MVA rating as a function of turbine flow.
    fp3_: PU  = None
 
    # Flow P4 (Fp4).  Turbine Flow value for point 4 for lookup table representing
    # per unit mechanical power on machine MVA rating as a function of turbine flow.
    fp4_: PU  = None
 
    # Flow P5 (Fp5).  Turbine Flow value for point 5 for lookup table representing
    # per unit mechanical power on machine MVA rating as a function of turbine flow.
    fp5_: PU  = None
 
    # Flow P6 (Fp6).  Turbine Flow value for point 6 for lookup table representing
    # per unit mechanical power on machine MVA rating as a function of turbine flow.
    fp6_: PU  = None
 
    # Flow P7 (Fp7).  Turbine Flow value for point 7 for lookup table representing
    # per unit mechanical power on machine MVA rating as a function of turbine flow.
    fp7_: PU  = None
 
    # Flow P8 (Fp8).  Turbine Flow value for point 8 for lookup table representing
    # per unit mechanical power on machine MVA rating as a function of turbine flow.
    fp8_: PU  = None
 
    # Flow P9 (Fp9).  Turbine Flow value for point 9 for lookup table representing
    # per unit mechanical power on machine MVA rating as a function of turbine flow.
    fp9_: PU  = None
 
    # Flow P10 (Fp10).  Turbine Flow value for point 10 for lookup table representing
    # per unit mechanical power on machine MVA rating as a function of turbine flow.
    fp10_: PU  = None
 
    # Pmss Flow P1 (Pmss1).  Mechanical Power output Pmss for Turbine Flow point 1
    # for lookup table representing per unit mechanical power on machine MVA rating
    # as a function of turbine flow.
    pmss1_: PU  = None
 
    # Pmss Flow P2 (Pmss2).  Mechanical Power output Pmss for Turbine Flow point 2
    # for lookup table representing per unit mechanical power on machine MVA rating
    # as a function of turbine flow.
    pmss2_: PU  = None
 
    # Pmss Flow P3 (Pmss3).  Mechanical Power output Pmss for Turbine Flow point 3
    # for lookup table representing per unit mechanical power on machine MVA rating
    # as a function of turbine flow.
    pmss3_: PU  = None
 
    # Pmss Flow P4 (Pmss4).  Mechanical Power output Pmss for Turbine Flow point 4
    # for lookup table representing per unit mechanical power on machine MVA rating
    # as a function of turbine flow.
    pmss4_: PU  = None
 
    # Pmss Flow P5 (Pmss5).  Mechanical Power output Pmss for Turbine Flow point 5
    # for lookup table representing per unit mechanical power on machine MVA rating
    # as a function of turbine flow.
    pmss5_: PU  = None
 
    # Pmss Flow P6 (Pmss6).  Mechanical Power output Pmss for Turbine Flow point 6
    # for lookup table representing per unit mechanical power on machine MVA rating
    # as a function of turbine flow.
    pmss6_: PU  = None
 
    # Pmss Flow P7 (Pmss7).  Mechanical Power output Pmss for Turbine Flow point 7
    # for lookup table representing per unit mechanical power on machine MVA rating
    # as a function of turbine flow.
    pmss7_: PU  = None
 
    # Pmss Flow P8 (Pmss8).  Mechanical Power output Pmss for Turbine Flow point 8
    # for lookup table representing per unit mechanical power on machine MVA rating
    # as a function of turbine flow.
    pmss8_: PU  = None
 
    # Pmss Flow P9 (Pmss9).  Mechanical Power output Pmss for Turbine Flow point 9
    # for lookup table representing per unit mechanical power on machine MVA rating
    # as a function of turbine flow.
    pmss9_: PU  = None
 
    # Pmss Flow P10 (Pmss10).  Mechanical Power output Pmss for Turbine Flow point 10
    # for lookup table representing per unit mechanical power on machine MVA rating
    # as a function of turbine flow.
    pmss10_: PU  = None
     