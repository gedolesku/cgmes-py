from __future__ import annotations
from .SynchronousMachineDynamics import SynchronousMachineDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class SynchronousMachineSimplified(SynchronousMachineDynamics):
    pass
