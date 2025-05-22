from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Core.Equipment import Equipment

@dataclass
class GeneratingUnit(Equipment):
    """A single or set of synchronous machines for converting mechanical power into
    alternating-current power. For example, individual machines within a set may be
    defined for scheduling purposes while a single control signal is derived for
    the set. In this case there would be a GeneratingUnit for each member of the
    set and an additional GeneratingUnit corresponding to the set.
    """
    # Generating unit economic participation factor.
    normalPF_: Simple_Float  = None
     