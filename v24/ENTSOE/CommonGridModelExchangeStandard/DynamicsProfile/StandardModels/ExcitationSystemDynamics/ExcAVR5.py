from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcAVR5(ExcitationSystemDynamics):
    """Manual excitation control with field circuit resistance. This model can be used
    as a very simple representation of manual voltage control.
    """
    # Gain (Ka).
    ka_: PU  = None
 
    # Time constant (Ta).
    ta_: Seconds  = None
 
    # Effective Output Resistance (Rex). Rex represents the effective output
    # resistance seen by the excitation system.
    rex_: PU  = None
     