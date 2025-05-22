from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.DiscontinuousExcitationControlDynamics.DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics

@dataclass
class DiscExcContIEEEDEC1A(DiscontinuousExcitationControlDynamics):
    """The class represents IEEE Type DEC1A discontinuous excitation control model
    that boosts generator excitation to a level higher than that demanded by the
    voltage regulator and stabilizer immediately following a system fault.
    
      Reference: IEEE Standard 421.5-2005 Section 12.2.
    """
    # Voltage reference (<i>V</i><i><sub>TLMT</sub></i>).  Typical Value = 1.1.
    vtlmt_: PU  = None
 
    # Limiter (<i>V</i><i><sub>OMAX</sub></i>).  Typical Value = 0.3.
    vomax_: PU  = None
 
    # Limiter (<i>V</i><i><sub>OMIN</sub></i>).  Typical Value = 0.1.
    vomin_: PU  = None
 
    # Terminal voltage limiter gain (<i>K</i><i><sub>ETL</sub></i>).  Typical Value =
    # 47.
    ketl_: PU  = None
 
    # Terminal voltage level reference (<i>V</i><i><sub>TC</sub></i>).  Typical Value
    # = 0.95.
    vtc_: PU  = None
 
    # Regulator voltage reference (<i>V</i><i><sub>AL</sub></i>).  Typical Value = 5.
    # 5.
    val_: PU  = None
 
    # Speed change reference (<i>E</i><i><sub>SC</sub></i>).  Typical Value = 0.0015.
    esc_: PU  = None
 
    # Discontinuous controller gain (<i>K</i><i><sub>AN</sub></i>).  Typical Value =
    # 400.
    kan_: PU  = None
 
    # Discontinuous controller time constant (<i>T</i><i><sub>AN</sub></i>).  Typical
    # Value = 0.08.
    tan_: Seconds  = None
 
    # DEC washout time constant (<i>T</i><i><sub>W</sub></i><sub>5</sub>).  Typical
    # Value = 5.
    tw5_: Seconds  = None
 
    # Limiter (<i>V</i><i><sub>SMAX</sub></i>).  Typical Value = 0.2.
    vsmax_: PU  = None
 
    # Limiter (<i>V</i><i><sub>SMIN</sub></i>).  Typical Value = -0.066.
    vsmin_: PU  = None
 
    # Time constant (<i>T</i><i><sub>D</sub></i>).  Typical Value = 0.03.
    td_: Seconds  = None
 
    # Time constant (<i>T</i><i><sub>L</sub></i><sub>1</sub>).  Typical Value = 0.025.
    tl1_: Seconds  = None
 
    # Time constant (<i>T</i><i><sub>L</sub></i><sub>2</sub>).  Typical Value = 1.25.
    tl2_: Seconds  = None
 
    # Voltage limits (<i>V</i><i><sub>TM</sub></i>).  Typical Value = 1.13.
    vtm_: PU  = None
 
    # Voltage limits (<i>V</i><i><sub>TN</sub></i>).  Typical Value = 1.12.
    vtn_: PU  = None
 
    # Limiter for Van (<i>V</i><i><sub>ANMAX</sub></i>).
    vanmax_: PU  = None
     