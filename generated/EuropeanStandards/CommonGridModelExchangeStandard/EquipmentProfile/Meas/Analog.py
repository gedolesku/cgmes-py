from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from .Measurement import Measurement
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class Analog(Measurement):
    positiveFlowIn: Optional[Boolean] = field(default=None, metadata={'xpath': 'cim:Analog.positiveFlowIn'})
