from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovSteamCC(TurbineGovernorDynamics):
    """Cross compound turbine governor model.
    """
    # Base for power values (MWbase) (>0).  Unit = MW.
    mwbase: ActivePower  = None
 
    # Maximum HP value position (Pmaxhp).  Typical Value = 1.
    pmaxhp: PU  = None
 
    # HP governor droop (Rhp).  Typical Value = 0.05.
    rhp: PU  = None
 
    # HP governor time constant (T1hp).  Typical Value = 0.1.
    t1hp: Seconds  = None
 
    # HP turbine time constant (T3hp).  Typical Value = 0.1.
    t3hp: Seconds  = None
 
    # HP turbine time constant (T4hp).  Typical Value = 0.1.
    t4hp: Seconds  = None
 
    # HP reheater time constant (T5hp).  Typical Value = 10.
    t5hp: Seconds  = None
 
    # Fraction of HP power ahead of reheater (Fhp).  Typical Value = 0.3.
    fhp: PU  = None
 
    # HP damping factor (Dhp).  Typical Value = 0.
    dhp: PU  = None
 
    # Maximum LP value position (Pmaxlp).  Typical Value = 1.
    pmaxlp: PU  = None
 
    # LP governor droop (Rlp).  Typical Value = 0.05.
    rlp: PU  = None
 
    # LP governor time constant (T1lp).  Typical Value = 0.1.
    t1lp: Seconds  = None
 
    # LP turbine time constant (T3lp).  Typical Value = 0.1.
    t3lp: Seconds  = None
 
    # LP turbine time constant (T4lp).  Typical Value = 0.1.
    t4lp: Seconds  = None
 
    # LP reheater time constant (T5lp).  Typical Value = 10.
    t5lp: Seconds  = None
 
    # Fraction of LP power ahead of reheater (Flp).  Typical Value = 0.7.
    flp: PU  = None
 
    # LP damping factor (Dlp).  Typical Value = 0.
    dlp: PU  = None
     