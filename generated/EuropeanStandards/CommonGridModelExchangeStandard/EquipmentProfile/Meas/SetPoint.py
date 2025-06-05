from __future__ import annotations
from ...DomainProfile.Simple_Float import Simple_Float
from .AnalogControl import AnalogControl
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class SetPoint(AnalogControl):
    normalValue: Simple_Float = field(metadata={'xpath': 'cim:SetPoint.normalValue'})
    value: Simple_Float = field(metadata={'xpath': 'cim:SetPoint.value'})
