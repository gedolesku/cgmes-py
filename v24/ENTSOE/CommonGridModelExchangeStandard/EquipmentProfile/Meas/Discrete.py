from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.ValueAliasSet import ValueAliasSet     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.Measurement import Measurement

@dataclass
class Discrete(Measurement):
    """Discrete represents a discrete Measurement, i.e. a Measurement representing
    discrete values, e.g. a Breaker position.
    """
    # The ValueAliasSet used for translation of a MeasurementValue.value to a name.
    ValueAliasSet_: Optional[ValueAliasSet] = None
     