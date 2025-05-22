from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.DiscreteValue import DiscreteValue     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.ValueAliasSet import ValueAliasSet     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.Control import Control

@dataclass
class Command(Control):
    """A Command is a discrete control used for supervisory control.
    """
    # Normal value for Control.value e.g. used for percentage scaling.
    normalValue: int  = None
 
    # The value representing the actuator output.
    value: int  = None
 
    # The Control variable associated with the MeasurementValue.
    DiscreteValue_ref: Optional[DiscreteValue] = None
    DiscreteValue: str = None
 
    # The ValueAliasSet used for translation of a Control value to a name.
    ValueAliasSet_ref: Optional[ValueAliasSet] = None
    ValueAliasSet: str = None
     