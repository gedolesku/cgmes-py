from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.CurrentFlow import CurrentFlow     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class Switch(ConductingEquipment):
    """A generic device designed to close, or open, or both, one or more electric
    circuits.  All switches are two terminal devices including grounding switches.
    """
    # The attribute is used in cases when no Measurement for the status value is
    # present. If the Switch has a status measurement the Discrete.normalValue is
    # expected to match with the Switch.normalOpen.
    normalOpen_: bool  = None
 
    # The maximum continuous current carrying capacity in amps governed by the device
    # material and construction.
    ratedCurrent_: CurrentFlow  = None
 
    # Branch is retained in a bus branch model.  The flow through retained switches
    # will normally be calculated in power flow.
    retained_: bool  = None
     