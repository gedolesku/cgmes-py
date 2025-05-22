from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.ValueAliasSet import ValueAliasSet     

@dataclass
class ValueToAlias(IdentifiedObject):
    """Describes the translation of one particular value into a name, e.g. 1 as "Open".
    """
    # The value that is mapped.
    value_: int  = None
 
    # The ValueToAlias mappings included in the set.
    ValueAliasSet_: Optional[ValueAliasSet] = None
     