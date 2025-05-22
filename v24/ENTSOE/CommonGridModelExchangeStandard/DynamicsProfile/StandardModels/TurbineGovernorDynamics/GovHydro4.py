from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Frequency import Frequency     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovHydro4(TurbineGovernorDynamics):
    """Hydro turbine and governor. Represents plants with straight-forward penstock
    configurations and hydraulic governors of traditional 'dashpot' type.  This
    model can be used to represent simple, Francis, Pelton or Kaplan turbines.
    """
    # Base for power values (MWbase) (>0).  Unit = MW.
    mwbase_: ActivePower  = None
 
    # Gate servo time constant (Tg) (>0).  Typical Value = 0.5.
    tg_: Seconds  = None
 
    # Pilot servo time constant (Tp).  Typical Value = 0.1.
    tp_: Seconds  = None
 
    # Max gate opening velocity (Uo).  Typical Vlaue = 0.2.
    uo_: Simple_Float  = None
 
    # Max gate closing velocity (Uc).  Typical Value = 0.2.
    uc_: Simple_Float  = None
 
    # Maximum gate opening, PU of MWbase (Gmax).  Typical Value = 1.
    gmax_: PU  = None
 
    # Minimum gate opening, PU of MWbase (Gmin).  Typical Value = 0.
    gmin_: PU  = None
 
    # Permanent droop (Rperm).  Typical Value = 0.05.
    rperm_: Seconds  = None
 
    # Temporary droop (Rtemp).  Typical Value = 0.3.
    rtemp_: Seconds  = None
 
    # Dashpot time constant (Tr) (>0).  Typical Value = 5.
    tr_: Seconds  = None
 
    # Water inertia time constant (Tw) (>0).  Typical Value = 1.
    tw_: Seconds  = None
 
    # Turbine gain (At).  Typical Value = 1.2.
    at_: PU  = None
 
    # Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed
    # (PU).
    # Typical Value = 0.5.  Typical Value Francis = 1.1, Kaplan = 1.1.
    dturb_: PU  = None
 
    # Head available at dam (hdam).  Typical Value = 1.
    hdam_: PU  = None
 
    # No-load flow at nominal head (Qnl).
    # Typical Value = 0.08.  Typical Value Francis = 0, Kaplan = 0.
    qn1_: PU  = None
 
    # Intentional deadband width (db1).  Unit = Hz.  Typical Value = 0.
    db1_: Frequency  = None
 
    # Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
    eps_: Frequency  = None
 
    # Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0.
    db2_: ActivePower  = None
 
    # Nonlinear gain point 0, PU gv (Gv0).
    # Typical Value = 0.  Typical Value Francis = 0.1, Kaplan = 0.1.
    gv0_: PU  = None
 
    # Nonlinear gain point 0, PU power (Pgv0).  Typical Value = 0.
    pgv0_: PU  = None
 
    # Nonlinear gain point 1, PU gv (Gv1).
    # Typical Value = 0.  Typical Value Francis = 0.4, Kaplan = 0.4.
    gv1_: PU  = None
 
    # Nonlinear gain point 1, PU power (Pgv1).
    # Typical Value = 0.  Typical Value Francis = 0.42, Kaplan = 0.35.
    pgv1_: PU  = None
 
    # Nonlinear gain point 2, PU gv (Gv2).
    # Typical Value = 0.  Typical Value Francis = 0.5, Kaplan = 0.5.
    gv2_: PU  = None
 
    # Nonlinear gain point 2, PU power (Pgv2).
    # Typical Value = 0.  Typical Value Francis = 0.56, Kaplan = 0.468.
    pgv2_: PU  = None
 
    # Nonlinear gain point 3, PU gv (Gv3).
    # Typical Value = 0.  Typical Value Francis = 0.7, Kaplan = 0.7.
    gv3_: PU  = None
 
    # Nonlinear gain point 3, PU power (Pgv3).
    # Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.796.
    pgv3_: PU  = None
 
    # Nonlinear gain point 4, PU gv (Gv4).
    # Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.8.
    gv4_: PU  = None
 
    # Nonlinear gain point 4, PU power (Pgv4).
    # Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.917.
    pgv4_: PU  = None
 
    # Nonlinear gain point 5, PU gv (Gv5).
    # Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.9.
    gv5_: PU  = None
 
    # Nonlinear gain point 5, PU power (Pgv5).
    # Typical Value = 0.  Typical Value Francis = 0.97, Kaplan = 0.99.
    pgv5_: PU  = None
 
    # Kaplan blade servo point 0 (Bgv0).  Typical Value = 0.
    bgv0_: PU  = None
 
    # Kaplan blade servo point 1 (Bgv1).  Typical Value = 0.
    bgv1_: PU  = None
 
    # Kaplan blade servo point 2 (Bgv2).
    # Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.1.
    bgv2_: PU  = None
 
    # Kaplan blade servo point 3 (Bgv3).
    # Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.667.
    bgv3_: PU  = None
 
    # Kaplan blade servo point 4 (Bgv4).
    # Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.9.
    bgv4_: PU  = None
 
    # Kaplan blade servo point 5 (Bgv5).
    # Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1.
    bgv5_: PU  = None
 
    # Maximum blade adjustment factor (Bmax).
    # Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1.1276.
    bmax_: Simple_Float  = None
 
    # Blade servo time constant (Tblade).  Typical Value = 100.
    tblade_: Seconds  = None
     