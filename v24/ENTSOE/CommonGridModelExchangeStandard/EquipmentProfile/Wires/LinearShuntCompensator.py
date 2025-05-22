from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Susceptance import Susceptance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Conductance import Conductance     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.ShuntCompensator import ShuntCompensator

@dataclass
class LinearShuntCompensator(ShuntCompensator):
    """A linear shunt compensator has banks or sections with equal admittance values.
    """
    # Zero sequence shunt (charging) susceptance per section
    b0PerSection_: Susceptance  = None
 
    # Positive sequence shunt (charging) susceptance per section
    bPerSection_: Susceptance  = None
 
    # Zero sequence shunt (charging) conductance per section
    g0PerSection_: Conductance  = None
 
    # Positive sequence shunt (charging) conductance per section
    gPerSection_: Conductance  = None
     