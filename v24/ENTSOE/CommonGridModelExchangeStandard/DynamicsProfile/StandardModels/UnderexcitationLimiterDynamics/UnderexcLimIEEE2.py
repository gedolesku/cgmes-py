from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.UnderexcitationLimiterDynamics.UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics

@dataclass
class UnderexcLimIEEE2(UnderexcitationLimiterDynamics):
    """The class represents the Type UEL2 which has either a straight-line or multi-
    segment characteristic when plotted in terms of machine reactive power output
    vs. real power output.
    
      Reference: IEEE UEL2 421.5-2005 Section 10.2.  (Limit characteristic lookup
    table shown in Figure 10.4 (p 32) of the standard).
    """
    # Voltage filter time constant (T<sub>UV</sub>).  Typical Value = 5.
    tuv_: Seconds  = None
 
    # Real power filter time constant (T<sub>UP</sub>).  Typical Value = 5.
    tup_: Seconds  = None
 
    # Reactive power filter time constant (T<sub>UQ</sub>).  Typical Value = 0.
    tuq_: Seconds  = None
 
    # UEL integral gain (K<sub>UI</sub>).  Typical Value = 0.5.
    kui_: PU  = None
 
    # UEL proportional gain (K<sub>UL</sub>).  Typical Value = 0.8.
    kul_: PU  = None
 
    # UEL integrator output maximum limit (V<sub>UIMAX</sub>).  Typical Value = 0.25.
    vuimax_: PU  = None
 
    # UEL integrator output minimum limit (V<sub>UIMIN</sub>).  Typical Value = 0.
    vuimin_: PU  = None
 
    # UEL excitation system stabilizer gain (K<sub>UF</sub>).  Typical Value = 0.
    kuf_: PU  = None
 
    # Gain associated with optional integrator feedback input signal to UEL
    # (K<sub>FB</sub>).  Typical Value = 0.
    kfb_: PU  = None
 
    # Time constant associated with optional integrator feedback input signal to UEL
    # (T<sub>UL</sub>).  Typical Value = 0.
    tul_: Seconds  = None
 
    # UEL lead time constant (T<sub>U1</sub>).  Typical Value = 0.
    tu1_: Seconds  = None
 
    # UEL lag time constant (T<sub>U2</sub>).  Typical Value = 0.
    tu2_: Seconds  = None
 
    # UEL lead time constant (T<sub>U3</sub>).  Typical Value = 0.
    tu3_: Seconds  = None
 
    # UEL lag time constant (T<sub>U4</sub>).  Typical Value = 0.
    tu4_: Seconds  = None
 
    # UEL output maximum limit (V<sub>ULMAX</sub>).  Typical Value = 0.25.
    vulmax_: PU  = None
 
    # UEL output minimum limit (V<sub>ULMIN</sub>).  Typical Value = 0.
    vulmin_: PU  = None
 
    # Real power values for endpoints (P<sub>0</sub>).  Typical Value = 0.
    p0_: PU  = None
 
    # Reactive power values for endpoints (Q<sub>0</sub>).  Typical Value = -0.31.
    q0_: PU  = None
 
    # Real power values for endpoints (P<sub>1</sub>).  Typical Value = 0.3.
    p1_: PU  = None
 
    # Reactive power values for endpoints (Q<sub>1</sub>).  Typical Value = -0.31.
    q1_: PU  = None
 
    # Real power values for endpoints (P<sub>2</sub>).  Typical Value = 0.6.
    p2_: PU  = None
 
    # Reactive power values for endpoints (Q<sub>2</sub>).  Typical Value = -0.28.
    q2_: PU  = None
 
    # Real power values for endpoints (P<sub>3</sub>).  Typical Value = 0.9.
    p3_: PU  = None
 
    # Reactive power values for endpoints (Q<sub>3</sub>).  Typical Value = -0.21.
    q3_: PU  = None
 
    # Real power values for endpoints (P<sub>4</sub>).  Typical Value = 1.02.
    p4_: PU  = None
 
    # Reactive power values for endpoints (Q<sub>4</sub>).  Typical Value = 0.
    q4_: PU  = None
 
    # Real power values for endpoints (P<sub>5</sub>). 
    p5_: PU  = None
 
    # Reactive power values for endpoints (Q<sub>5</sub>). 
    q5_: PU  = None
 
    # Real power values for endpoints (P<sub>6</sub>).
    p6_: PU  = None
 
    # Reactive power values for endpoints (Q<sub>6</sub>). 
    q6_: PU  = None
 
    # Real power values for endpoints (P<sub>7</sub>). 
    p7_: PU  = None
 
    # Reactive power values for endpoints (Q<sub>7</sub>). 
    q7_: PU  = None
 
    # Real power values for endpoints (P<sub>8</sub>). 
    p8_: PU  = None
 
    # Reactive power values for endpoints (Q<sub>8</sub>). 
    q8_: PU  = None
 
    # Real power values for endpoints (P<sub>9</sub>). 
    p9_: PU  = None
 
    # Reactive power values for endpoints (Q<sub>9</sub>). 
    q9_: PU  = None
 
    # Real power values for endpoints (P<sub>10</sub>). 
    p10_: PU  = None
 
    # Reactive power values for endpoints (Q<sub>10</sub>). 
    q10_: PU  = None
 
    # UEL terminal voltage exponent applied to real power input to UEL limit look-up
    # table (k1).  Typical Value = 2.
    k1_: Simple_Float  = None
 
    # UEL terminal voltage exponent applied to reactive power output from UEL limit
    # look-up table (k2).  Typical Value = 2.
    k2_: Simple_Float  = None
     