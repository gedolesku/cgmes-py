from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Susceptance import Susceptance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Conductance import Conductance     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Equivalents.EquivalentEquipment import EquivalentEquipment

@dataclass
class EquivalentShunt(EquivalentEquipment):
    """The class represents equivalent shunts.
    """
    # Positive sequence shunt susceptance.
    b_: Susceptance  = None
 
    # Positive sequence shunt conductance.
    g_: Conductance  = None
     