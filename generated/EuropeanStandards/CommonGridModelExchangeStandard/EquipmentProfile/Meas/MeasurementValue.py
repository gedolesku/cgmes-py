from __future__ import annotations
from ...DomainProfile.DateTime import DateTime
from ...DomainProfile.PerCent import PerCent
from ..Core.IdentifiedObject import IdentifiedObject
from .MeasurementValueSource import MeasurementValueSource
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class MeasurementValue(Protocol):
    MeasurementValueSource_ref: MeasurementValueSource  # metadata: cim='cim:MeasurementValue.MeasurementValueSource', mult='1'
    MeasurementValueSource_id: str
    sensorAccuracy: Optional[PerCent]  # metadata: cim='cim:MeasurementValue.sensorAccuracy', mult='0..1'
    timeStamp: Optional[DateTime]  # metadata: cim='cim:MeasurementValue.timeStamp', mult='0..1'
