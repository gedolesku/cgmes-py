from __future__ import annotations
from ...DomainProfile.CurrentFlow import CurrentFlow
from .Connector import Connector
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class BusbarSection(Connector):
    ipMax: Optional[CurrentFlow] = field(default=None, metadata={'xpath': 'cim:BusbarSection.ipMax'})
