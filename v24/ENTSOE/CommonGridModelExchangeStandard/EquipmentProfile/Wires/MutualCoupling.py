from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Susceptance import Susceptance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Length import Length     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Conductance import Conductance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Reactance import Reactance     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Terminal import Terminal     

@dataclass
class MutualCoupling(IdentifiedObject):
    """This class represents the zero sequence line mutual coupling.
    """
    # Zero sequence mutual coupling shunt (charging) susceptance, uniformly
    # distributed, of the entire line section.
    b0ch_: Susceptance  = None
 
    # Distance to the start of the coupled region from the first line's terminal
    # having sequence number equal to 1.
    distance11_: Length  = None
 
    # Distance to the end of the coupled region from the first line's terminal with
    # sequence number equal to 1.
    distance12_: Length  = None
 
    # Distance to the start of coupled region from the second line's terminal with
    # sequence number equal to 1.
    distance21_: Length  = None
 
    # Distance to the end of coupled region from the second line's terminal with
    # sequence number equal to 1.
    distance22_: Length  = None
 
    # Zero sequence mutual coupling shunt (charging) conductance, uniformly
    # distributed, of the entire line section.
    g0ch_: Conductance  = None
 
    # Zero sequence branch-to-branch mutual impedance coupling, resistance.
    r0_: Resistance  = None
 
    # Zero sequence branch-to-branch mutual impedance coupling, reactance.
    x0_: Reactance  = None
 
    # The starting terminal for the calculation of distances along the first branch
    # of the mutual coupling.  Normally MutualCoupling would only be used for
    # terminals of AC line segments.  The first and second terminals of a mutual
    # coupling should point to different AC line segments.
    Terminal_: Optional[Terminal] = None
 
    # The starting terminal for the calculation of distances along the second branch
    # of the mutual coupling.
    Terminal_: Optional[Terminal] = None
     