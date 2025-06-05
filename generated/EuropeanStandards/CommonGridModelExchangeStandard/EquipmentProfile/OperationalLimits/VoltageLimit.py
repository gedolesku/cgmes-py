from __future__ import annotations
from ...DomainProfile.Voltage import Voltage
from .OperationalLimit import OperationalLimit
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class VoltageLimit(OperationalLimit):
    value: Voltage = field(metadata={'xpath': 'cim:VoltageLimit.value'})
