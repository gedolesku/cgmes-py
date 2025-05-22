from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcST6BOELselectorKind import ExcST6BOELselectorKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEST6B(ExcitationSystemDynamics):
    """The class represents IEEE Std 421.5-2005 type ST6B model. This model consists
    of a PI voltage regulator with an inner loop field voltage regulator and pre-
    control. The field voltage regulator implements a proportional control. The pre-
    control and the delay in the feedback circuit increase the dynamic response.
    
      Reference: IEEE Standard 421.5-2005 Section 7.6.
    """
    # Exciter output current limit reference (I<sub>LR</sub>).  Typical Value = 4.164.
    ilr_: PU  = None
 
    # Exciter output current limit adjustment (K<sub>CI</sub>).  Typical Value = 1.
    # 0577.
    kci_: PU  = None
 
    # Pre-control gain constant of the inner loop field regulator (K<sub>FF</sub>).
    # Typical Value = 1.
    kff_: PU  = None
 
    # Feedback gain constant of the inner loop field regulator (K<sub>G</sub>).
    # Typical Value = 1.
    kg_: PU  = None
 
    # Voltage regulator integral gain (K<sub>IA</sub>).  Typical Value = 45.094.
    kia_: PU  = None
 
    # Exciter output current limiter gain (K<sub>LR</sub>).  Typical Value = 17.33.
    klr_: PU  = None
 
    # Forward gain constant of the inner loop field regulator (K<sub>M</sub>).
    # Typical Value = 1.
    km_: PU  = None
 
    # Voltage regulator proportional gain (K<sub>PA</sub>).  Typical Value = 18.038.
    kpa_: PU  = None
 
    # OEL input selector (OELin). Typical Value = noOELinput.
    oelin_: ExcST6BOELselectorKind  = None
 
    # Feedback time constant of inner loop field voltage regulator (T<sub>G</sub>).
    # Typical Value = 0.02.
    tg_: Seconds  = None
 
    # Maximum voltage regulator output (V<sub>AMAX</sub>).  Typical Value = 4.81.
    vamax_: PU  = None
 
    # Minimum voltage regulator output (V<sub>AMIN</sub>).  Typical Value = -3.85.
    vamin_: PU  = None
 
    # Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 4.81.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -3.85.
    vrmin_: PU  = None
     