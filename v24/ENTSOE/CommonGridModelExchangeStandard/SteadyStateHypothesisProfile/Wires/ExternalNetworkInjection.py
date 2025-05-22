from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ReactivePower import ReactivePower     
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.RegulatingCondEq import RegulatingCondEq

@dataclass
class ExternalNetworkInjection(RegulatingCondEq):
    """This class represents external network and it is used for IEC 60909
    calculations.
    """
    # Priority of unit for use as powerflow voltage phase angle reference bus
    # selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and
    # so on.
    referencePriority_: int  = None
 
    # Active power injection. Load sign convention is used, i.e. positive sign means
    # flow out from a node.
    # Starting value for steady state solutions.
    p_: ActivePower  = None
 
    # Reactive power injection. Load sign convention is used, i.e. positive sign
    # means flow out from a node.
    # Starting value for steady state solutions.
    q_: ReactivePower  = None
     