from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ReactivePower import ReactivePower     
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class EnergySource(ConductingEquipment):
    """A generic equivalent for an energy supplier on a transmission or distribution
    voltage level.
    """
    # High voltage source active injection. Load sign convention is used, i.e.
    # positive sign means flow out from a node.
    # Starting value for steady state solutions.
    activePower_: ActivePower  = None
 
    # High voltage source reactive injection. Load sign convention is used, i.e.
    # positive sign means flow out from a node.
    # Starting value for steady state solutions.
    reactivePower_: ReactivePower  = None
     