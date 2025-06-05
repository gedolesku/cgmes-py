from __future__ import annotations
from .LoadDynamics import LoadDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class LoadAggregate(LoadDynamics):
    pass
