from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from .OperationalLimit import OperationalLimit
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ActivePowerLimit(OperationalLimit):
    value: ActivePower = field(metadata={'xpath': 'cim:ActivePowerLimit.value'})
