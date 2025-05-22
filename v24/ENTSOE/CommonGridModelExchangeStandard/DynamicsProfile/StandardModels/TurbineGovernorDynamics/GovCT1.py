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
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovCT1(TurbineGovernorDynamics):
    """General model for any prime mover with a PID governor, used primarily for
    combustion turbine and combined cycle units.
      This model can be used to represent a variety of prime movers controlled by
    PID governors.  It is suitable, for example, for representation of
      <ul>
      	<li>gas turbine and single shaft combined cycle turbines </li>
      </ul>
      <ul>
      	<li>diesel engines with modern electronic or digital governors  </li>
      </ul>
      <ul>
      	<li>steam turbines where steam is supplied from a large boiler drum or a
    large header whose pressure is substantially constant over the period under
    study </li>
      	<li>simple hydro turbines in dam configurations where the water column
    length is short and water inertia effects are minimal. </li>
      </ul>
      Additional information on this model is available in the 2012 IEEE report,
    <i><u>Dynamic Models for Turbine-Governors in Power System Studies</u></i>,
    section 3.1.2.3 page 3-4 (GGOV1).
    """
    # Base for power values (MWbase) (> 0).  Unit = MW.
    mwbase_: ActivePower  = None
 
    # Permanent droop (R).  Typical Value = 0.04.
    r_: PU  = None
 
    # Feedback signal for droop (Rselect).  Typical Value = electricalPower.
    rselect_: DroopSignalFeedbackKind  = None
 
    # Electrical power transducer time constant (Tpelec) (>0).  Typical Value = 1.
    tpelec_: Seconds  = None
 
    # Maximum value for speed error signal (maxerr).  Typical Value = 0.05.
    maxerr_: PU  = None
 
    # Minimum value for speed error signal (minerr).  Typical Value = -0.05.
    minerr_: PU  = None
 
    # Governor proportional gain (Kpgov).  Typical Value = 10.
    kpgov_: PU  = None
 
    # Governor integral gain (Kigov).  Typical Value = 2.
    kigov_: PU  = None
 
    # Governor derivative gain (Kdgov).  Typical Value = 0.
    kdgov_: PU  = None
 
    # Governor derivative controller time constant (Tdgov).  Typical Value = 1.
    tdgov_: Seconds  = None
 
    # Maximum valve position limit (Vmax).  Typical Value = 1.
    vmax_: PU  = None
 
    # Minimum valve position limit (Vmin).  Typical Value = 0.15.
    vmin_: PU  = None
 
    # Actuator time constant (Tact).  Typical Value = 0.5.
    tact_: Seconds  = None
 
    # Turbine gain (Kturb) (>0).  Typical Value = 1.5.
    kturb_: PU  = None
 
    # No load fuel flow (Wfnl).  Typical Value = 0.2.
    wfnl_: PU  = None
 
    # Turbine lag time constant (Tb) (>0).  Typical Value = 0.5.
    tb_: Seconds  = None
 
    # Turbine lead time constant (Tc).  Typical Value = 0.
    tc_: Seconds  = None
 
    # Switch for fuel source characteristic to recognize that fuel flow, for a given
    # fuel valve stroke, can be proportional to engine speed (Wfspd).
    # true = fuel flow proportional to speed (for some gas turbines and diesel
    # engines with positive displacement fuel injectors)
    # false = fuel control system keeps fuel flow independent of engine speed.
    # Typical Value = true.
    wfspd_: bool  = None
 
    # Transport time delay for diesel engine used in representing diesel engines
    # where there is a small but measurable transport delay between a change in fuel
    # flow setting and the development of torque (Teng).  Teng should be zero in all
    # but special cases where this transport delay is of particular concern.  Typical
    # Value = 0.
    teng_: Seconds  = None
 
    # Load Limiter time constant (Tfload) (>0).  Typical Value = 3.
    tfload_: Seconds  = None
 
    # Load limiter proportional gain for PI controller (Kpload).  Typical Value = 2.
    kpload_: PU  = None
 
    # Load limiter integral gain for PI controller (Kiload).  Typical Value = 0.67.
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
 
    # Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 0.10.
    ropen_: Simple_Float  = None
 
    # Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -0.1.
    rclose_: Simple_Float  = None
 
    # Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to
    # a reset time of 100 seconds.  A value of 0.001 corresponds to a relatively slow
    # acting load controller.  Typical Value = 0.01.
    kimw_: PU  = None
 
    # Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 0.01.
    aset_: Simple_Float  = None
 
    # Acceleration limiter gain (Ka).  Typical Value = 10.
    ka_: PU  = None
 
    # Acceleration limiter time constant (Ta) (>0).  Typical Value = 0.1.
    ta_: Seconds  = None
 
    # Speed governor dead band in per unit speed (db).  In the majority of
    # applications, it is recommended that this value be set to zero.  Typical Value
    # = 0.
    db_: PU  = None
 
    # Temperature detection lead time constant (Tsa).  Typical Value = 4.
    tsa_: Seconds  = None
 
    # Temperature detection lag time constant (Tsb).  Typical Value = 5.
    tsb_: Seconds  = None
 
    # Maximum rate of load limit increase (Rup).  Typical Value = 99.
    rup_: PU  = None
 
    # Maximum rate of load limit decrease (Rdown).  Typical Value = -99.
    rdown_: PU  = None
     