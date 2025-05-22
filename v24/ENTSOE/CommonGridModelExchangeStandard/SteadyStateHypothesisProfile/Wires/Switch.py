from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class Switch(ConductingEquipment):
    """A generic device designed to close, or open, or both, one or more electric
    circuits.  All switches are two terminal devices including grounding switches.
    """
    # The attribute tells if the switch is considered open when used as input to
    # topology processing.
    open_: bool  = None
     