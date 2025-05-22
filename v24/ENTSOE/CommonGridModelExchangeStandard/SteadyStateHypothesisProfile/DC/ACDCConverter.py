from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ReactivePower import ReactivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class ACDCConverter(ConductingEquipment):
    """A unit with valves for three phases, together with unit control equipment,
    essential protective and switching devices, DC storage capacitors, phase
    reactors and auxiliaries, if any, used for conversion.
    """
    # Active power at the point of common coupling. Load sign convention is used, i.e.
    # positive sign means flow out from a node.
    # Starting value for a steady state solution in the case a simplified power flow
    # model is used.
    p: ActivePower  = None
 
    # Reactive power at the point of common coupling. Load sign convention is used, i.
    # e. positive sign means flow out from a node.
    # Starting value for a steady state solution in the case a simplified power flow
    # model is used.
    q: ReactivePower  = None
 
    # Real power injection target in AC grid, at point of common coupling.
    targetPpcc: ActivePower  = None
 
    # Target value for DC voltage magnitude.
    targetUdc: Voltage  = None
     