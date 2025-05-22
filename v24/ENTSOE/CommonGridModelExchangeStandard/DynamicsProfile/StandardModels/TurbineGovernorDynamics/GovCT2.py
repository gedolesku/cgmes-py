from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.DroopSignalFeedbackKind import DroopSignalFeedbackKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Frequency import Frequency     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovCT2(TurbineGovernorDynamics):
    """General governor model with frequency-dependent fuel flow limit.  This model is
    a modification of the GovCT1<b> </b>model in order to represent the frequency-
    dependent fuel flow limit of a specific gas turbine manufacturer.
    """
    # Base for power values (MWbase) (> 0).  Unit = MW.
    mwbase_: ActivePower  = None
 
    # Permanent droop (R).  Typical Value = 0.05.
    r_: PU  = None
 
    # Feedback signal for droop (Rselect).  Typical Value = electricalPower.
    rselect_: DroopSignalFeedbackKind  = None
 
    # Electrical power transducer time constant (Tpelec).  Typical Value = 2.5.
    tpelec_: Seconds  = None
 
    # Maximum value for speed error signal (Maxerr).  Typical Value = 1.
    maxerr_: PU  = None
 
    # Minimum value for speed error signal (Minerr).  Typical Value = -1.
    minerr_: PU  = None
 
    # Governor proportional gain (Kpgov).  Typical Value = 4.
    kpgov_: PU  = None
 
    # Governor integral gain (Kigov).  Typical Value = 0.45.
    kigov_: PU  = None
 
    # Governor derivative gain (Kdgov).  Typical Value = 0.
    kdgov_: PU  = None
 
    # Governor derivative controller time constant (Tdgov).  Typical Value = 1.
    tdgov_: Seconds  = None
 
    # Maximum valve position limit (Vmax).  Typical Value = 1.
    vmax_: PU  = None
 
    # Minimum valve position limit (Vmin).  Typical Value = 0.175.
    vmin_: PU  = None
 
    # Actuator time constant (Tact).  Typical Value = 0.4.
    tact_: Seconds  = None
 
    # Turbine gain (Kturb).  Typical Value = 1.9168.
    kturb_: PU  = None
 
    # No load fuel flow (Wfnl).  Typical Value = 0.187.
    wfnl_: PU  = None
 
    # Turbine lag time constant (Tb).  Typical Value = 0.1.
    tb_: Seconds  = None
 
    # Turbine lead time constant (Tc).  Typical Value = 0.
    tc_: Seconds  = None
 
    # Switch for fuel source characteristic to recognize that fuel flow, for a given
    # fuel valve stroke, can be proportional to engine speed (Wfspd).
    # true = fuel flow proportional to speed (for some gas turbines and diesel
    # engines with positive displacement fuel injectors)
    # false = fuel control system keeps fuel flow independent of engine speed.
    # Typical Value = false.
    wfspd_: bool  = None
 
    # Transport time delay for diesel engine used in representing diesel engines
    # where there is a small but measurable transport delay between a change in fuel
    # flow setting and the development of torque (Teng).  Teng should be zero in all
    # but special cases where this transport delay is of particular concern.  Typical
    # Value = 0.
    teng_: Seconds  = None
 
    # Load Limiter time constant (Tfload).  Typical Value = 3.
    tfload_: Seconds  = None
 
    # Load limiter proportional gain for PI controller (Kpload).  Typical Value = 1.
    kpload_: PU  = None
 
    # Load limiter integral gain for PI controller (Kiload).  Typical Value = 1.
    kiload_: PU  = None
 
    # Load limiter reference value (Ldref).  Typical Value = 1.
    ldref_: PU  = None
 
    # Speed sensitivity coefficient (Dm).  Dm can represent either the variation of
    # the engine power with the shaft speed or the variation of maximum power
    # capability with shaft speed.  If it is positive it describes the falling slope
    # of the engine speed verses power characteristic as speed increases. A slightly
    # falling characteristic is typical for reciprocating engines and some aero-
    # derivative turbines.  If it is negative the engine power is assumed to be
    # unaffected by the shaft speed, but the maximum permissible fuel flow is taken
    # to fall with falling shaft speed. This is characteristic of single-shaft
    # industrial turbines due to exhaust temperature limits.  Typical Value = 0.
    dm_: PU  = None
 
    # Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 99.
    ropen_: Simple_Float  = None
 
    # Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -99.
    rclose_: Simple_Float  = None
 
    # Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to
    # a reset time of 100 seconds.  A value of 0.001 corresponds to a relatively slow
    # acting load controller.  Typical Value = 0.
    kimw_: PU  = None
 
    # Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 10.
    aset_: Simple_Float  = None
 
    # Acceleration limiter Gain (Ka).  Typical Value = 10.
    ka_: PU  = None
 
    # Acceleration limiter time constant (Ta).  Typical Value = 1.
    ta_: Seconds  = None
 
    # Speed governor dead band in per unit speed (db).  In the majority of
    # applications, it is recommended that this value be set to zero.  Typical Value
    # = 0.
    db_: PU  = None
 
    # Temperature detection lead time constant (Tsa).  Typical Value = 0.
    tsa_: Seconds  = None
 
    # Temperature detection lag time constant (Tsb).  Typical Value = 50.
    tsb_: Seconds  = None
 
    # Maximum rate of load limit increase (Rup).  Typical Value = 99.
    rup_: PU  = None
 
    # Maximum rate of load limit decrease (Rdown).  Typical Value = -99.
    rdown_: PU  = None
 
    # Ramp rate for frequency-dependent power limit (Prate).  Typical Value = 0.017.
    prate_: PU  = None
 
    # Frequency threshold 1 (Flim1).  Unit = Hz.  Typical Value = 59.
    flim1_: Frequency  = None
 
    # Power limit 1 (Plim1).  Typical Value = 0.8325.
    plim1_: PU  = None
 
    # Frequency threshold 2 (Flim2).  Unit = Hz.  Typical Value = 0.
    flim2_: Frequency  = None
 
    # Power limit 2 (Plim2).  Typical Value = 0.
    plim2_: PU  = None
 
    # Frequency threshold 3 (Flim3).  Unit = Hz.  Typical Value = 0.
    flim3_: Frequency  = None
 
    # Power limit 3 (Plim3).  Typical Value = 0.
    plim3_: PU  = None
 
    # Frequency threshold 4 (Flim4).  Unit = Hz.  Typical Value = 0.
    flim4_: Frequency  = None
 
    # Power limit 4 (Plim4).  Typical Value = 0.
    plim4_: PU  = None
 
    # Frequency threshold 5 (Flim5).  Unit = Hz.  Typical Value = 0.
    flim5_: Frequency  = None
 
    # Power limit 5 (Plim5).  Typical Value = 0.
    plim5_: PU  = None
 
    # Frequency threshold 6 (Flim6).  Unit = Hz.  Typical Value = 0.
    flim6_: Frequency  = None
 
    # Power limit 6 (Plim6).  Typical Value = 0.
    plim6_: PU  = None
 
    # Frequency threshold 7 (Flim7).  Unit = Hz.  Typical Value = 0.
    flim7_: Frequency  = None
 
    # Power limit 7 (Plim7).  Typical Value = 0.
    plim7_: PU  = None
 
    # Frequency threshold 8 (Flim8).  Unit = Hz.  Typical Value = 0.
    flim8_: Frequency  = None
 
    # Power limit 8 (Plim8).  Typical Value = 0.
    plim8_: PU  = None
 
    # Frequency threshold 9 (Flim9).  Unit = Hz.  Typical Value = 0.
    flim9_: Frequency  = None
 
    # Power Limit 9 (Plim9).  Typical Value = 0.
    plim9_: PU  = None
 
    # Frequency threshold 10 (Flim10).  Unit = Hz.  Typical Value = 0.
    flim10_: Frequency  = None
 
    # Power limit 10 (Plim10).  Typical Value = 0.
    plim10_: PU  = None
     