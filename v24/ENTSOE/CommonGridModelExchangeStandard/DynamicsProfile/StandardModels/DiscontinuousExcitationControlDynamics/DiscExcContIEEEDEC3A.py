from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.DiscontinuousExcitationControlDynamics.DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics

@dataclass
class DiscExcContIEEEDEC3A(DiscontinuousExcitationControlDynamics):
    """The class represents IEEE Type DEC3A model. In some systems, the stabilizer
    output is disconnected from the regulator immediately following a severe fault
    to prevent the stabilizer from competing with action of voltage regulator
    during the first swing.
    
      Reference: IEEE Standard 421.5-2005 Section 12.4.
    """
    # Terminal undervoltage comparison level (<i>V</i><i><sub>TMIN</sub></i>). 
    vtmin: PU  = None
 
    # Reset time delay (<i>T</i><i><sub>DR</sub></i>). 
    tdr: Seconds  = None
     