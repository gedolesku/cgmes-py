from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.AngleDegrees import AngleDegrees     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.StateVariablesProfile.Topology.TopologicalNode import TopologicalNode     

@dataclass
class SvVoltage:
    """State variable for voltage.
    """
    # The voltage angle of the topological node complex voltage with respect to
    # system reference.
    angle_: AngleDegrees  = None
 
    # The voltage magnitude of the topological node.
    v_: Voltage  = None
 
    # The state voltage associated with the topological node.
    TopologicalNode_: Optional[TopologicalNode] = None
     