from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Core.PowerSystemResource import PowerSystemResource

@dataclass
class ControlArea(PowerSystemResource):
    """A control area<b> </b>is a grouping of generating units and/or loads and a
    cutset of tie lines (as terminals) which may be used for a variety of purposes
    including automatic generation control, powerflow solution area interchange
    control specification, and input to load forecasting.   Note that any number of
    overlapping control area specifications can be superimposed on the physical
    model.
    """
    # The specified positive net interchange into the control area, i.e. positive
    # sign means flow in to the area.
    netInterchange: ActivePower  = None
 
    # Active power net interchange tolerance
    pTolerance: ActivePower  = None
     