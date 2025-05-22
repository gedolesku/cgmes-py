from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovGAST4(TurbineGovernorDynamics):
    """Generic turbogas.
    """
    # Droop (bp).  Typical Value = 0.05.
    bp_: PU  = None
 
    # Time constant of fuel valve positioner (T<sub>y</sub>).  Typical Value = 0.1.
    tv_: Seconds  = None
 
    # Maximum gate opening velocity (T<sub>A</sub>).  Typical Value = 3.
    ta_: Seconds  = None
 
    # Maximum gate closing velocity (T<sub>c</sub>).  Typical Value = 0.5.
    tc_: Seconds  = None
 
    # Fuel control time constant (T<sub>cm</sub>).  Typical Value = 0.1.
    tcm_: Seconds  = None
 
    # Compressor gain (K<sub>tm</sub>).  Typical Value = 0.
    ktm_: PU  = None
 
    # Compressor discharge volume time constant (T<sub>m</sub>).  Typical Value = 0.2.
    tm_: Seconds  = None
 
    # Maximum valve opening (RYMX).  Typical Value = 1.1.
    rymx_: PU  = None
 
    # Minimum valve opening (RYMN).  Typical Value = 0.
    rymn_: PU  = None
 
    # Fuel flow maximum positive error value (MX<sub>EF</sub>).  Typical Value = 0.05.
    mxef_: PU  = None
 
    # Fuel flow maximum negative error value (MN<sub>EF</sub>).  Typical Value = -0.
    # 05.
    mnef_: PU  = None
     