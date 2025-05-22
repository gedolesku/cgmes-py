from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.OverexcitationLimiterDynamics.OverexcitationLimiterDynamics import OverexcitationLimiterDynamics

@dataclass
class OverexcLimX2(OverexcitationLimiterDynamics):
    """Field Voltage or Current overexcitation limiter designed to protect the
    generator field of an AC machine with automatic excitation control from
    overheating due to prolonged overexcitation.
    """
    # (m).
    # true = IFD limiting
    # false = EFD limiting.
    m_: bool  = None
 
    # Rated field voltage if m=F or field current if m=T (EFD<sub>RATED</sub>).
    # Typical Value = 1.05.
    efdrated_: PU  = None
 
    # Low voltage or current point on the inverse time characteristic
    # (EFD<sub>1</sub>).  Typical Value = 1.1.
    efd1_: PU  = None
 
    # Time to trip the exciter at the low voltage or current point on the inverse
    # time characteristic (TIME<sub>1</sub>).  Typical Value = 120.
    t1_: Seconds  = None
 
    # Mid voltage or current point on the inverse time characteristic
    # (EFD<sub>2</sub>).  Typical Value = 1.2.
    efd2_: PU  = None
 
    # Time to trip the exciter at the mid voltage or current point on the inverse
    # time characteristic (TIME<sub>2</sub>).  Typical Value = 40.
    t2_: Seconds  = None
 
    # High voltage or current point on the inverse time characteristic
    # (EFD<sub>3</sub>).  Typical Value = 1.5.
    efd3_: PU  = None
 
    # Time to trip the exciter at the high voltage or current point on the inverse
    # time characteristic (TIME<sub>3</sub>).  Typical Value = 15.
    t3_: Seconds  = None
 
    # Desired field voltage if m=F or field current if m=T (EFD<sub>DES</sub>).
    # Typical Value = 1.
    efddes_: PU  = None
 
    # Gain (K<sub>MX</sub>).  Typical Value = 0.002.
    kmx_: PU  = None
 
    # Low voltage limit (V<sub>LOW</sub>) (>0).
    vlow_: PU  = None
     