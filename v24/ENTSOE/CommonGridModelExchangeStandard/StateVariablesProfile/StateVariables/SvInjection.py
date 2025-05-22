from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ReactivePower import ReactivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.StateVariablesProfile.Topology.TopologicalNode import TopologicalNode     

@dataclass
class SvInjection:
    """The SvInjection is reporting the calculated bus injection minus the sum of the
    terminal flows. The terminal flow is positive out from the bus (load sign
    convention) and bus injection has positive flow into the bus. SvInjection may
    have the remainder after state estimation or slack after power flow calculation.
    """
    # The active power injected into the bus in addition to injections from equipment
    # terminals.  Positive sign means injection into the TopologicalNode (bus).
    pInjection_: ActivePower  = None
 
    # The reactive power injected into the bus in addition to injections from
    # equipment terminals. Positive sign means injection into the TopologicalNode
    # (bus).
    qInjection_: ReactivePower  = None
 
    # The injection flows state variables associated with the topological node.
    TopologicalNode_: Optional[TopologicalNode] = None
     