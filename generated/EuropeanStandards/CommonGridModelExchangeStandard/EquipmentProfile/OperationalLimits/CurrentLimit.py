from __future__ import annotations
from ...DomainProfile.CurrentFlow import CurrentFlow
from .OperationalLimit import OperationalLimit
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class CurrentLimit(OperationalLimit):
    value: CurrentFlow = field(metadata={'xpath': 'cim:CurrentLimit.value'})
