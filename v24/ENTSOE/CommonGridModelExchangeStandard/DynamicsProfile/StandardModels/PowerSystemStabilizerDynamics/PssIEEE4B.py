from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
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
    bwh1: Simple_Float  = None
 
    # Notch filter 2 (high-frequency band): Three dB bandwidth (B<sub>wi</sub>). 
    bwh2: Simple_Float  = None
 
    # Notch filter 1 (low-frequency band): Three dB bandwidth (B<sub>wi</sub>). 
    bwl1: Simple_Float  = None
 
    # Notch filter 2 (low-frequency band): Three dB bandwidth (B<sub>wi</sub>). 
    bwl2: Simple_Float  = None
 
    # High band gain (K<sub>H</sub>).  Typical Value = 120.
    kh: PU  = None
 
    # High band differential filter gain (K<sub>H1</sub>).  Typical Value = 66.
    kh1: PU  = None
 
    # High band first lead-lag blocks coefficient (K<sub>H11</sub>).  Typical Value =
    # 1.
    kh11: PU  = None
 
    # High band first lead-lag blocks coefficient (K<sub>H17</sub>).  Typical Value =
    # 1.
    kh17: PU  = None
 
    # High band differential filter gain (K<sub>H2</sub>).  Typical Value = 66.
    kh2: PU  = None
 
    # Intermediate band gain (K<sub>I</sub>).  Typical Value = 30.
    ki: PU  = None
 
    # Intermediate band differential filter gain (K<sub>I1</sub>).  Typical Value =
    # 66.
    ki1: PU  = None
 
    # Intermediate band first lead-lag blocks coefficient (K<sub>I11</sub>).  Typical
    # Value = 1.
    ki11: PU  = None
 
    # Intermediate band first lead-lag blocks coefficient (K<sub>I17</sub>).  Typical
    # Value = 1.
    ki17: PU  = None
 
    # Intermediate band differential filter gain (K<sub>I2</sub>).  Typical Value =
    # 66.
    ki2: PU  = None
 
    # Low band gain (K<sub>L</sub>).  Typical Value = 7.5.
    kl: PU  = None
 
    # Low band differential filter gain (K<sub>L1</sub>).  Typical Value = 66.
    kl1: PU  = None
 
    # Low band first lead-lag blocks coefficient (K<sub>L11</sub>).  Typical Value =
    # 1.
    kl11: PU  = None
 
    # Low band first lead-lag blocks coefficient (K<sub>L17</sub>).  Typical Value =
    # 1.
    kl17: PU  = None
 
    # Low band differential filter gain (K<sub>L2</sub>).  Typical Value = 66.
    kl2: PU  = None
 
    # Notch filter 1 (high-frequency band): filter frequency (omega<sub>ni</sub>).
    omeganh1: Simple_Float  = None
 
    # Notch filter 2 (high-frequency band): filter frequency (omega<sub>ni</sub>).
    omeganh2: Simple_Float  = None
 
    # Notch filter 1 (low-frequency band): filter frequency (omega<sub>ni</sub>).
    omeganl1: Simple_Float  = None
 
    # Notch filter 2 (low-frequency band): filter frequency (omega<sub>ni</sub>).
    omeganl2: Simple_Float  = None
 
    # High band time constant (T<sub>H1</sub>).  Typical Value = 0.01513.
    th1: Seconds  = None
 
    # High band time constant (T<sub>H10</sub>).  Typical Value = 0.
    th10: Seconds  = None
 
    # High band time constant (T<sub>H11</sub>).  Typical Value = 0.
    th11: Seconds  = None
 
    # High band time constant (T<sub>H12</sub>).  Typical Value = 0.
    th12: Seconds  = None
 
    # High band time constant (T<sub>H2</sub>).  Typical Value = 0.01816.
    th2: Seconds  = None
 
    # High band time constant (T<sub>H3</sub>).  Typical Value = 0.
    th3: Seconds  = None
 
    # High band time constant (T<sub>H4</sub>).  Typical Value = 0.
    th4: Seconds  = None
 
    # High band time constant (T<sub>H5</sub>).  Typical Value = 0.
    th5: Seconds  = None
 
    # High band time constant (T<sub>H6</sub>).  Typical Value = 0.
    th6: Seconds  = None
 
    # High band time constant (T<sub>H7</sub>).  Typical Value = 0.01816.
    th7: Seconds  = None
 
    # High band time constant (T<sub>H8</sub>).  Typical Value = 0.02179.
    th8: Seconds  = None
 
    # High band time constant (T<sub>H9</sub>).  Typical Value = 0.
    th9: Seconds  = None
 
    # Intermediate band time constant (T<sub>I1</sub>).  Typical Value = 0.173.
    ti1: Seconds  = None
 
    # Intermediate band time constant (T<sub>I11</sub>).  Typical Value = 0.
    ti10: Seconds  = None
 
    # Intermediate band time constant (T<sub>I11</sub>).  Typical Value = 0.
    ti11: Seconds  = None
 
    # Intermediate band time constant (T<sub>I2</sub>).  Typical Value = 0.
    ti12: Seconds  = None
 
    # Intermediate band time constant (T<sub>I2</sub>).  Typical Value = 0.2075.
    ti2: Seconds  = None
 
    # Intermediate band time constant (T<sub>I3</sub>).  Typical Value = 0.
    ti3: Seconds  = None
 
    # Intermediate band time constant (T<sub>I4</sub>).  Typical Value = 0.
    ti4: Seconds  = None
 
    # Intermediate band time constant (T<sub>I5</sub>).  Typical Value = 0.
    ti5: Seconds  = None
 
    # Intermediate band time constant (T<sub>I6</sub>).  Typical Value = 0.
    ti6: Seconds  = None
 
    # Intermediate band time constant (T<sub>I7</sub>).  Typical Value = 0.2075.
    ti7: Seconds  = None
 
    # Intermediate band time constant (T<sub>I8</sub>).  Typical Value = 0.2491.
    ti8: Seconds  = None
 
    # Intermediate band time constant (T<sub>I9</sub>).  Typical Value = 0.
    ti9: Seconds  = None
 
    # Low band time constant (T<sub>L1</sub>).  Typical Value = 1.73.
    tl1: Seconds  = None
 
    # Low band time constant (T<sub>L10</sub>).  Typical Value = 0.
    tl10: Seconds  = None
 
    # Low band time constant (T<sub>L11</sub>).  Typical Value = 0.
    tl11: Seconds  = None
 
    # Low band time constant (T<sub>L12</sub>).  Typical Value = 0.
    tl12: Seconds  = None
 
    # Low band time constant (T<sub>L2</sub>).  Typical Value = 2.075.
    tl2: Seconds  = None
 
    # Low band time constant (T<sub>L3</sub>).  Typical Value = 0.
    tl3: Seconds  = None
 
    # Low band time constant (T<sub>L4</sub>).  Typical Value = 0.
    tl4: Seconds  = None
 
    # Low band time constant (T<sub>L5</sub>).  Typical Value = 0.
    tl5: Seconds  = None
 
    # Low band time constant (T<sub>L6</sub>).  Typical Value = 0.
    tl6: Seconds  = None
 
    # Low band time constant (T<sub>L7</sub>).  Typical Value = 2.075.
    tl7: Seconds  = None
 
    # Low band time constant (T<sub>L8</sub>).  Typical Value = 2.491.
    tl8: Seconds  = None
 
    # Low band time constant (T<sub>L9</sub>).  Typical Value = 0.
    tl9: Seconds  = None
 
    # High band output maximum limit (V<sub>Hmax</sub>).  Typical Value = 0.6.
    vhmax: PU  = None
 
    # High band output minimum limit (V<sub>Hmin</sub>).  Typical Value = -0.6.
    vhmin: PU  = None
 
    # Intermediate band output maximum limit (V<sub>Imax</sub>).  Typical Value = 0.6.
    vimax: PU  = None
 
    # Intermediate band output minimum limit (V<sub>Imin</sub>).  Typical Value = -0.
    # 6.
    vimin: PU  = None
 
    # Low band output maximum limit (V<sub>Lmax</sub>).  Typical Value = 0.075.
    vlmax: PU  = None
 
    # Low band output minimum limit (V<sub>Lmin</sub>).  Typical Value = -0.075.
    vlmin: PU  = None
 
    # PSS output maximum limit (V<sub>STmax</sub>).  Typical Value = 0.15.
    vstmax: PU  = None
 
    # PSS output minimum limit (V<sub>STmin</sub>).  Typical Value = -0.15.
    vstmin: PU  = None
     