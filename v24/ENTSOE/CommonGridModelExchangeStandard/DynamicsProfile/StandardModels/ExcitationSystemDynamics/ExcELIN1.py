from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcELIN1(ExcitationSystemDynamics):
    """Static PI transformer fed excitation system: ELIN (VATECH) - simplified model.
    This model represents an all-static excitation system. A PI voltage controller
    establishes a desired field current set point for a proportional current
    controller. The integrator of the PI controller has a follow-up input to match
    its signal to the present field current.  A power system stabilizer with power
    input is included in the model.
    """
    # Current transducer time constant (Tfi).  Typical Value = 0.
    tfi_: Seconds  = None
 
    # Controller reset time constant (Tnu).  Typical Value = 2.
    tnu_: Seconds  = None
 
    # Voltage controller proportional gain (Vpu).  Typical Value = 34.5.
    vpu_: PU  = None
 
    # Current controller gain (Vpi).  Typical Value = 12.45.
    vpi_: PU  = None
 
    # Controller follow up gain (Vpnf).  Typical Value = 2.
    vpnf_: PU  = None
 
    # Controller follow up dead band (Dpnf).  Typical Value = 0.
    dpnf_: PU  = None
 
    # Stabilizer parameters (Tsw).  Typical Value = 3.
    tsw_: Seconds  = None
 
    # Minimum open circuit excitation voltage (Efmin).  Typical Value = -5.
    efmin_: PU  = None
 
    # Maximum open circuit excitation voltage (Efmax).  Typical Value = 5.
    efmax_: PU  = None
 
    # Excitation transformer effective reactance (Xe) (>=0).  Xe represents the
    # regulation of the transformer/rectifier unit.  Typical Value = 0.06.
    xe_: PU  = None
 
    # Stabilizer Gain 1 (Ks1).  Typical Value = 0.
    ks1_: PU  = None
 
    # Stabilizer Gain 2 (Ks2).  Typical Value = 0.
    ks2_: PU  = None
 
    # Stabilizer Phase Lag Time Constant (Ts1).  Typical Value = 1.
    ts1_: Seconds  = None
 
    # Stabilizer Filter Time Constant (Ts2).  Typical Value = 1.
    ts2_: Seconds  = None
 
    # Stabilizer Limit Output (smax).  Typical Value = 0.1.
    smax_: PU  = None
     