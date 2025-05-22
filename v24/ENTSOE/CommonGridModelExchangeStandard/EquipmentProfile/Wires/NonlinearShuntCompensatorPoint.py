from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Susceptance import Susceptance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Conductance import Conductance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     

@dataclass
class NonlinearShuntCompensatorPoint:
    """A non linear shunt compensator bank or section admittance value.
    """
    # Positive sequence shunt (charging) susceptance per section
    b_: Susceptance  = None
 
    # Zero sequence shunt (charging) susceptance per section
    b0_: Susceptance  = None
 
    # Positive sequence shunt (charging) conductance per section
    g_: Conductance  = None
 
    # Zero sequence shunt (charging) conductance per section
    g0_: Conductance  = None
 
    # The number of the section.
    sectionNumber_: int  = None
     