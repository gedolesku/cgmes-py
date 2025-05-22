from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.DiscontinuousExcitationControlDynamics.DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics

@dataclass
class DiscExcContIEEEDEC2A(DiscontinuousExcitationControlDynamics):
    """The class represents IEEE Type DEC2A model for the discontinuous excitation
    control. This system provides transient excitation boosting via an open-loop
    control as initiated by a trigger signal generated remotely.
    
      Reference: IEEE Standard 421.5-2005 Section 12.3.
    """
    # Discontinuous controller input reference (<i>V</i><i><sub>K</sub></i>). 
    vk_: PU  = None
 
    # Discontinuous controller time constant (<i>T</i><i><sub>D1</sub></i>). 
    td1_: Seconds  = None
 
    # Discontinuous controller washout time constant (<i>T</i><i><sub>D2</sub></i>). 
    td2_: Seconds  = None
 
    # Limiter (<i>V</i><i><sub>DMIN</sub></i>). 
    vdmin_: PU  = None
 
    # Limiter (<i>V</i><i><sub>DMAX</sub></i>). 
    vdmax_: PU  = None
     