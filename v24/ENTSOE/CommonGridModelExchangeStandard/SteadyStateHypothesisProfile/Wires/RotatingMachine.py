from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ReactivePower import ReactivePower     
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.RegulatingCondEq import RegulatingCondEq

@dataclass
class RotatingMachine(RegulatingCondEq):
    """A rotating machine which may be used as a generator or motor.
    """
    # Active power injection. Load sign convention is used, i.e. positive sign means
    # flow out from a node.
    # Starting value for a steady state solution.
    p_: ActivePower  = None
 
    # Reactive power injection. Load sign convention is used, i.e. positive sign
    # means flow out from a node.
    # Starting value for a steady state solution.
    q_: ReactivePower  = None
     