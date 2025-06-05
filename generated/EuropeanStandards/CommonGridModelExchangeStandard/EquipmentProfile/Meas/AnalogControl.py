from __future__ import annotations
from ...DomainProfile.Simple_Float import Simple_Float
from .AnalogValue import AnalogValue
from .Control import Control
from typing import Protocol, runtime_checkable

@runtime_checkable
class AnalogControl(Control, Protocol):
    maxValue: Simple_Float  # metadata: cim='cim:AnalogControl.maxValue', mult='1'
    minValue: Simple_Float  # metadata: cim='cim:AnalogControl.minValue', mult='1'
    AnalogValue_ref: AnalogValue  # metadata: cim='cim:AnalogControl.AnalogValue', mult='1'
    AnalogValue_id: str
