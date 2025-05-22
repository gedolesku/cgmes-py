from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Reactance import Reactance     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Terminal import Terminal     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.BaseVoltage import BaseVoltage     

@dataclass
class TransformerEnd(IdentifiedObject):
    """A conducting connection point of a power transformer. It corresponds to a
    physical transformer winding terminal.  In earlier CIM versions, the
    TransformerWinding class served a similar purpose, but this class is more
    flexible because it associates to terminal but is not a specialization of
    ConductingEquipment.
    """
    # (for Yn and Zn connections) Resistance part of neutral impedance where
    # 'grounded' is true.
    rground_: Resistance  = None
 
    # Number for this transformer end, corresponding to the end's order in the power
    # transformer vector group or phase angle clock number.  Highest voltage winding
    # should be 1.  Each end within a power transformer should have a unique
    # subsequent end number.   Note the transformer end number need not match the
    # terminal sequence number.
    endNumber_: int  = None
 
    # (for Yn and Zn connections) True if the neutral is solidly grounded.
    grounded_: bool  = None
 
    # (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded'
    # is true.
    xground_: Reactance  = None
 
    # Terminal of the power transformer to which this transformer end belongs.
    Terminal_: Optional[Terminal] = None
 
    # Base voltage of the transformer end.  This is essential for PU calculation.
    BaseVoltage_: Optional[BaseVoltage] = None
     