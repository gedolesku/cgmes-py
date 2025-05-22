from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class RegulatingCondEq(ConductingEquipment):
    """A type of conducting equipment that can regulate a quantity (i.e. voltage or
    flow) at a specific point in the network.
    """
    # Specifies the regulation status of the equipment.  True is regulating, false is
    # not regulating.
    controlEnabled: bool  = None
     