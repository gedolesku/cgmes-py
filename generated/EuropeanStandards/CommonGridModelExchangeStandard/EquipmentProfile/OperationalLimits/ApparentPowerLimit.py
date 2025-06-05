from __future__ import annotations
from ...DomainProfile.ApparentPower import ApparentPower
from .OperationalLimit import OperationalLimit
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ApparentPowerLimit(OperationalLimit):
    value: ApparentPower = field(metadata={'xpath': 'cim:ApparentPowerLimit.value'})
