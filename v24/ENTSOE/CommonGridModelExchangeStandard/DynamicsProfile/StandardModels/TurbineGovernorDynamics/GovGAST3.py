from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Temperature import Temperature     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovGAST3(TurbineGovernorDynamics):
    """Generic turbogas with acceleration and temperature controller.
    """
    # Droop (bp).  Typical Value = 0.05.
    bp_: PU  = None
 
    # Time constant of speed governor (Tg).  Typical Value = 0.05.
    tg_: Seconds  = None
 
    # Maximum fuel flow (RCMX).  Typical Value = 1.
    rcmx_: PU  = None
 
    # Minimum fuel flow (RCMN).  Typical Value = -0.1.
    rcmn_: PU  = None
 
    # Coefficient of transfer function of fuel valve positioner (Ky).  Typical Value
    # = 1.
    ky_: Simple_Float  = None
 
    # Time constant of fuel valve positioner (Ty).  Typical Value = 0.2.
    ty_: Seconds  = None
 
    # Fuel control time constant (Tac).  Typical Value = 0.1.
    tac_: Seconds  = None
 
    # Fuel system feedback (K<sub>AC</sub>).  Typical Value = 0.
    kac_: Simple_Float  = None
 
    # Compressor discharge volume time constant (Tc).  Typical Value = 0.2.
    tc_: Seconds  = None
 
    # Acceleration limit set-point (Bca).  Unit = 1/s.  Typical Value = 0.01.
    bca_: Simple_Float  = None
 
    # Acceleration control integral gain (Kca). Unit = 1/s.  Typical Value = 100.
    kca_: Simple_Float  = None
 
    # Exhaust temperature variation due to fuel flow increasing from 0 to 1 PU
    # (deltaTc).  Typical Value = 390.
    dtc_: Temperature  = None
 
    # Minimum fuel flow (Ka).  Typical Value = 0.23.
    ka_: PU  = None
 
    # Time constant of radiation shield (Tsi).  Typical Value = 15.
    tsi_: Seconds  = None
 
    # Gain of radiation shield (Ksi).  Typical Value = 0.8.
    ksi_: Simple_Float  = None
 
    # Time constant of thermocouple (Ttc).  Typical Value = 2.5.
    ttc_: Seconds  = None
 
    # Turbine rated exhaust temperature correspondent to Pm=1 PU (Tfen).  Typical
    # Value = 540.
    tfen_: Temperature  = None
 
    # Temperature controller derivative gain (Td).  Typical Value = 3.3.
    td_: Seconds  = None
 
    # Temperature controller integration rate (Tt).  Typical Value = 250.
    tt_: Temperature  = None
 
    # Fuel flow maximum positive error value (MX<sub>EF</sub>).  Typical Value = 0.05.
    mxef_: PU  = None
 
    # Fuel flow maximum negative error value (MN<sub>EF</sub>).  Typical Value = -0.
    # 05.
    mnef_: PU  = None
     