from __future__ import annotations
from .Measurement import Measurement
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class Accumulator(Measurement):
    pass
