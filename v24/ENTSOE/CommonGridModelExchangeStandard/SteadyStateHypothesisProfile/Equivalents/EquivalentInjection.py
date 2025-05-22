from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ReactivePower import ReactivePower     
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Equivalents.EquivalentEquipment import EquivalentEquipment

@dataclass
class EquivalentInjection(EquivalentEquipment):
    """This class represents equivalent injections (generation or load).  Voltage
    regulation is allowed only at the point of connection.
    """
    # Specifies the default regulation status of the EquivalentInjection.  True is
    # regulating.  False is not regulating.
    regulationStatus_: bool  = None
 
    # The target voltage for voltage regulation.
    regulationTarget_: Voltage  = None
 
    # Equivalent active power injection. Load sign convention is used, i.e. positive
    # sign means flow out from a node.
    # Starting value for steady state solutions.
    p_: ActivePower  = None
 
    # Equivalent reactive power injection. Load sign convention is used, i.e.
    # positive sign means flow out from a node.
    # Starting value for steady state solutions.
    q_: ReactivePower  = None
     