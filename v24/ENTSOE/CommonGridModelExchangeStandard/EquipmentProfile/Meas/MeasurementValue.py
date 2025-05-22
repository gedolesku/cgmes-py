from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.DateTime import DateTime     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PerCent import PerCent     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Meas.MeasurementValueSource import MeasurementValueSource     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class MeasurementValue(IdentifiedObject):
    """The current state for a measurement. A state value is an instance of a
    measurement from a specific source. Measurements can be associated with many
    state values, each representing a different source for the measurement.
    """
    # The time when the value was last updated
    timeStamp_: DateTime  = None
 
    # The limit, expressed as a percentage of the sensor maximum, that errors will
    # not exceed when the sensor is used under  reference conditions.
    sensorAccuracy_: PerCent  = None
 
    # The MeasurementValues updated by the source.
    MeasurementValueSource_: Optional[MeasurementValueSource] = None
     