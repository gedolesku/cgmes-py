from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class Pss1(PowerSystemStabilizerDynamics):
    """Italian PSS - three input PSS (speed, frequency, power).
    """
    # Shaft speed power input gain (K<sub>W</sub>).  Typical Value = 0.
    kw_: Simple_Float  = None
 
    # Frequency power input gain (K<sub>F</sub>).  Typical Value = 5.
    kf_: Simple_Float  = None
 
    # Electric power input gain (K<sub>PE</sub>).  Typical Value = 0.3.
    kpe_: Simple_Float  = None
 
    # Minimum power PSS enabling (P<sub>MIN</sub>).  Typical Value = 0.25.
    pmin_: PU  = None
 
    # PSS gain (K<sub>S</sub>).  Typical Value = 1.
    ks_: Simple_Float  = None
 
    # Stabilizer output max limit (V<sub>SMN</sub>).  Typical Value = -0.06.
    vsmn_: PU  = None
 
    # Stabilizer output min limit (V<sub>SMX</sub>).  Typical Value = 0.06.
    vsmx_: PU  = None
 
    # Electric power filter time constant (T<sub>PE</sub>).  Typical Value = 0.05.
    tpe_: Seconds  = None
 
    # Washout (T<sub>5</sub>).  Typical Value = 3.5.
    t5_: Seconds  = None
 
    # Filter time constant (T<sub>6</sub>).  Typical Value = 0.
    t6_: Seconds  = None
 
    # Lead/lag time constant (T<sub>7</sub>).  Typical Value = 0.
    t7_: Seconds  = None
 
    # Lead/lag time constant (T<sub>8</sub>).  Typical Value = 0.
    t8_: Seconds  = None
 
    # Lead/lag time constant (T<sub>9</sub>).  Typical Value = 0.
    t9_: Seconds  = None
 
    # Lead/lag time constant (T<sub>10</sub>).  Typical Value = 0.
    t10_: Seconds  = None
 
    # <font color="#0f0f0f">Signal selector (V<sub>adAt</sub>).</font>
    # <font color="#0f0f0f">true = closed (Generator Power is greater than
    # Pmin)</font>
    # <font color="#0f0f0f">false = open (Pe is smaller than Pmin).</font>
    # <font color="#0f0f0f">Typical Value = true.</font>
    vadat_: bool  = None
     