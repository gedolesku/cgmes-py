from __future__ import annotations
from ...DomainProfile.DateTime import DateTime
from ...DomainProfile.Seconds import Seconds
from .BasicIntervalSchedule import BasicIntervalSchedule
from typing import Protocol, runtime_checkable

@runtime_checkable
class RegularIntervalSchedule(BasicIntervalSchedule, Protocol):
    endTime: DateTime  # metadata: cim='cim:RegularIntervalSchedule.endTime', mult='1'
    timeStep: Seconds  # metadata: cim='cim:RegularIntervalSchedule.timeStep', mult='1'
