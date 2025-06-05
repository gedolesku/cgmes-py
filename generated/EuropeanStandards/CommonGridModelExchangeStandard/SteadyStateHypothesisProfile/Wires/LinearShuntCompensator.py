from __future__ import annotations
from .ShuntCompensator import ShuntCompensator
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class LinearShuntCompensator(ShuntCompensator):
    pass
