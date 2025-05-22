from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ReactivePower import ReactivePower     
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.RegulatingCondEq import RegulatingCondEq

@dataclass
class StaticVarCompensator(RegulatingCondEq):
    """A facility for providing variable and controllable shunt reactive power. The
    SVC typically consists of a stepdown transformer, filter, thyristor-controlled
    reactor, and thyristor-switched capacitor arms.
    
      The SVC may operate in fixed MVar output mode or in voltage control mode.
    When in voltage control mode, the output of the SVC will be proportional to the
    deviation of voltage at the controlled bus from the voltage setpoint.  The SVC
    characteristic slope defines the proportion.  If the voltage at the controlled
    bus is equal to the voltage setpoint, the SVC MVar output is zero.
    """
    # Reactive power injection. Load sign convention is used, i.e. positive sign
    # means flow out from a node.
    # Starting value for a steady state solution.
    q: ReactivePower  = None
     