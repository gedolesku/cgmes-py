from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class PssIEEE4B(PowerSystemStabilizerDynamics):
    """The class represents IEEE Std 421.5-2005 type PSS2B power system stabilizer
    model. The PSS4B model represents a structure based on multiple working
    frequency bands. Three separate bands, respectively dedicated to the low-,
    intermediate- and high-frequency modes of oscillations, are used in this delta-
    omega (speed input) PSS.
    
      Reference: IEEE 4B 421.5-2005 Section 8.4.
    """
    # Notch filter 1 (high-frequency band): Three dB bandwidth (B<sub>wi</sub>). 
    bwh1_: Simple_Float  = None
 
    # Notch filter 2 (high-frequency band): Three dB bandwidth (B<sub>wi</sub>). 
    bwh2_: Simple_Float  = None
 
    # Notch filter 1 (low-frequency band): Three dB bandwidth (B<sub>wi</sub>). 
    bwl1_: Simple_Float  = None
 
    # Notch filter 2 (low-frequency band): Three dB bandwidth (B<sub>wi</sub>). 
    bwl2_: Simple_Float  = None
 
    # High band gain (K<sub>H</sub>).  Typical Value = 120.
    kh_: PU  = None
 
    # High band differential filter gain (K<sub>H1</sub>).  Typical Value = 66.
    kh1_: PU  = None
 
    # High band first lead-lag blocks coefficient (K<sub>H11</sub>).  Typical Value =
    # 1.
    kh11_: PU  = None
 
    # High band first lead-lag blocks coefficient (K<sub>H17</sub>).  Typical Value =
    # 1.
    kh17_: PU  = None
 
    # High band differential filter gain (K<sub>H2</sub>).  Typical Value = 66.
    kh2_: PU  = None
 
    # Intermediate band gain (K<sub>I</sub>).  Typical Value = 30.
    ki_: PU  = None
 
    # Intermediate band differential filter gain (K<sub>I1</sub>).  Typical Value =
    # 66.
    ki1_: PU  = None
 
    # Intermediate band first lead-lag blocks coefficient (K<sub>I11</sub>).  Typical
    # Value = 1.
    ki11_: PU  = None
 
    # Intermediate band first lead-lag blocks coefficient (K<sub>I17</sub>).  Typical
    # Value = 1.
    ki17_: PU  = None
 
    # Intermediate band differential filter gain (K<sub>I2</sub>).  Typical Value =
    # 66.
    ki2_: PU  = None
 
    # Low band gain (K<sub>L</sub>).  Typical Value = 7.5.
    kl_: PU  = None
 
    # Low band differential filter gain (K<sub>L1</sub>).  Typical Value = 66.
    kl1_: PU  = None
 
    # Low band first lead-lag blocks coefficient (K<sub>L11</sub>).  Typical Value =
    # 1.
    kl11_: PU  = None
 
    # Low band first lead-lag blocks coefficient (K<sub>L17</sub>).  Typical Value =
    # 1.
    kl17_: PU  = None
 
    # Low band differential filter gain (K<sub>L2</sub>).  Typical Value = 66.
    kl2_: PU  = None
 
    # Notch filter 1 (high-frequency band): filter frequency (omega<sub>ni</sub>).
    omeganh1_: Simple_Float  = None
 
    # Notch filter 2 (high-frequency band): filter frequency (omega<sub>ni</sub>).
    omeganh2_: Simple_Float  = None
 
    # Notch filter 1 (low-frequency band): filter frequency (omega<sub>ni</sub>).
    omeganl1_: Simple_Float  = None
 
    # Notch filter 2 (low-frequency band): filter frequency (omega<sub>ni</sub>).
    omeganl2_: Simple_Float  = None
 
    # High band time constant (T<sub>H1</sub>).  Typical Value = 0.01513.
    th1_: Seconds  = None
 
    # High band time constant (T<sub>H10</sub>).  Typical Value = 0.
    th10_: Seconds  = None
 
    # High band time constant (T<sub>H11</sub>).  Typical Value = 0.
    th11_: Seconds  = None
 
    # High band time constant (T<sub>H12</sub>).  Typical Value = 0.
    th12_: Seconds  = None
 
    # High band time constant (T<sub>H2</sub>).  Typical Value = 0.01816.
    th2_: Seconds  = None
 
    # High band time constant (T<sub>H3</sub>).  Typical Value = 0.
    th3_: Seconds  = None
 
    # High band time constant (T<sub>H4</sub>).  Typical Value = 0.
    th4_: Seconds  = None
 
    # High band time constant (T<sub>H5</sub>).  Typical Value = 0.
    th5_: Seconds  = None
 
    # High band time constant (T<sub>H6</sub>).  Typical Value = 0.
    th6_: Seconds  = None
 
    # High band time constant (T<sub>H7</sub>).  Typical Value = 0.01816.
    th7_: Seconds  = None
 
    # High band time constant (T<sub>H8</sub>).  Typical Value = 0.02179.
    th8_: Seconds  = None
 
    # High band time constant (T<sub>H9</sub>).  Typical Value = 0.
    th9_: Seconds  = None
 
    # Intermediate band time constant (T<sub>I1</sub>).  Typical Value = 0.173.
    ti1_: Seconds  = None
 
    # Intermediate band time constant (T<sub>I11</sub>).  Typical Value = 0.
    ti10_: Seconds  = None
 
    # Intermediate band time constant (T<sub>I11</sub>).  Typical Value = 0.
    ti11_: Seconds  = None
 
    # Intermediate band time constant (T<sub>I2</sub>).  Typical Value = 0.
    ti12_: Seconds  = None
 
    # Intermediate band time constant (T<sub>I2</sub>).  Typical Value = 0.2075.
    ti2_: Seconds  = None
 
    # Intermediate band time constant (T<sub>I3</sub>).  Typical Value = 0.
    ti3_: Seconds  = None
 
    # Intermediate band time constant (T<sub>I4</sub>).  Typical Value = 0.
    ti4_: Seconds  = None
 
    # Intermediate band time constant (T<sub>I5</sub>).  Typical Value = 0.
    ti5_: Seconds  = None
 
    # Intermediate band time constant (T<sub>I6</sub>).  Typical Value = 0.
    ti6_: Seconds  = None
 
    # Intermediate band time constant (T<sub>I7</sub>).  Typical Value = 0.2075.
    ti7_: Seconds  = None
 
    # Intermediate band time constant (T<sub>I8</sub>).  Typical Value = 0.2491.
    ti8_: Seconds  = None
 
    # Intermediate band time constant (T<sub>I9</sub>).  Typical Value = 0.
    ti9_: Seconds  = None
 
    # Low band time constant (T<sub>L1</sub>).  Typical Value = 1.73.
    tl1_: Seconds  = None
 
    # Low band time constant (T<sub>L10</sub>).  Typical Value = 0.
    tl10_: Seconds  = None
 
    # Low band time constant (T<sub>L11</sub>).  Typical Value = 0.
    tl11_: Seconds  = None
 
    # Low band time constant (T<sub>L12</sub>).  Typical Value = 0.
    tl12_: Seconds  = None
 
    # Low band time constant (T<sub>L2</sub>).  Typical Value = 2.075.
    tl2_: Seconds  = None
 
    # Low band time constant (T<sub>L3</sub>).  Typical Value = 0.
    tl3_: Seconds  = None
 
    # Low band time constant (T<sub>L4</sub>).  Typical Value = 0.
    tl4_: Seconds  = None
 
    # Low band time constant (T<sub>L5</sub>).  Typical Value = 0.
    tl5_: Seconds  = None
 
    # Low band time constant (T<sub>L6</sub>).  Typical Value = 0.
    tl6_: Seconds  = None
 
    # Low band time constant (T<sub>L7</sub>).  Typical Value = 2.075.
    tl7_: Seconds  = None
 
    # Low band time constant (T<sub>L8</sub>).  Typical Value = 2.491.
    tl8_: Seconds  = None
 
    # Low band time constant (T<sub>L9</sub>).  Typical Value = 0.
    tl9_: Seconds  = None
 
    # High band output maximum limit (V<sub>Hmax</sub>).  Typical Value = 0.6.
    vhmax_: PU  = None
 
    # High band output minimum limit (V<sub>Hmin</sub>).  Typical Value = -0.6.
    vhmin_: PU  = None
 
    # Intermediate band output maximum limit (V<sub>Imax</sub>).  Typical Value = 0.6.
    vimax_: PU  = None
 
    # Intermediate band output minimum limit (V<sub>Imin</sub>).  Typical Value = -0.
    # 6.
    vimin_: PU  = None
 
    # Low band output maximum limit (V<sub>Lmax</sub>).  Typical Value = 0.075.
    vlmax_: PU  = None
 
    # Low band output minimum limit (V<sub>Lmin</sub>).  Typical Value = -0.075.
    vlmin_: PU  = None
 
    # PSS output maximum limit (V<sub>STmax</sub>).  Typical Value = 0.15.
    vstmax_: PU  = None
 
    # PSS output minimum limit (V<sub>STmin</sub>).  Typical Value = -0.15.
    vstmin_: PU  = None
     