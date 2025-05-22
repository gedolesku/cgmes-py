from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class Pss5(PowerSystemStabilizerDynamics):
    """Italian PSS - Detailed PSS.
    """
    # Electric power input gain (K<sub>PE</sub>).  Typical Value = 0.3.
    kpe: Simple_Float  = None
 
    # Frequency/shaft speed input gain (K<sub>F</sub>).  Typical Value = 5.
    kf: Simple_Float  = None
 
    # Selector for Frequency/shaft speed input (IsFreq).
    # true = speed
    # false = frequency.
    # Typical Value = true.
    isfreq: bool  = None
 
    # PSS gain (K<sub>PSS</sub>).  Typical Value = 1.
    kpss: Simple_Float  = None
 
    # Selector for Second washout enabling (C<sub>TW2</sub>).
    # true = second washout filter is bypassed
    # false = second washout filter in use.
    # Typical Value = true.
    ctw2: bool  = None
 
    # First WashOut (T<sub>w1</sub>).  Typical Value = 3.5.
    tw1: Seconds  = None
 
    # Second WashOut (T<sub>w2</sub>).  Typical Value = 0.
    tw2: Seconds  = None
 
    # Lead/lag time constant (T<sub>L1</sub>).  Typical Value = 0.
    tl1: Seconds  = None
 
    # Lead/lag time constant (T<sub>L2</sub>).  Typical Value = 0.
    tl2: Seconds  = None
 
    # Lead/lag time constant (T<sub>L3</sub>).  Typical Value = 0.
    tl3: Seconds  = None
 
    # Lead/lag time constant (T<sub>L4</sub>).  Typical Value = 0.
    tl4: Seconds  = None
 
    # Stabilizer output max limit (V<sub>SMN</sub>).  Typical Value = -0.1.
    vsmn: PU  = None
 
    # Stabilizer output min limit (V<sub>SMX</sub>).  Typical Value = 0.1.
    vsmx: PU  = None
 
    # Electric power filter time constant (T<sub>PE</sub>).  Typical Value = 0.05.
    tpe: Seconds  = None
 
    # Minimum power PSS enabling (P<sub>mn</sub>).  Typical Value = 0.25.
    pmm: PU  = None
 
    # Stabilizer output dead band (DeadBand).  Typical Value = 0.
    deadband: PU  = None
 
    # <font color="#0f0f0f">Signal selector (V<sub>adAtt</sub>).</font>
    # <font color="#0f0f0f">true = closed (Generator Power is greater than
    # Pmin)</font>
    # <font color="#0f0f0f">false = open (Pe is smaller than Pmin).</font>
    # <font color="#0f0f0f">Typical Value = true.</font>
    vadat: bool  = None
     