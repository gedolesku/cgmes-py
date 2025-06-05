from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .AsynchronousMachineDynamics import AsynchronousMachineDynamics
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class AsynchronousMachineTimeConstantReactance(AsynchronousMachineDynamics):
    tpo: Optional[Seconds] = field(default=None, metadata={'xpath': 'cim:AsynchronousMachineTimeConstantReactance.tpo'})
    tppo: Optional[Seconds] = field(default=None, metadata={'xpath': 'cim:AsynchronousMachineTimeConstantReactance.tppo'})
    xp: Optional[PU] = field(default=None, metadata={'xpath': 'cim:AsynchronousMachineTimeConstantReactance.xp'})
    xpp: Optional[PU] = field(default=None, metadata={'xpath': 'cim:AsynchronousMachineTimeConstantReactance.xpp'})
    xs: Optional[PU] = field(default=None, metadata={'xpath': 'cim:AsynchronousMachineTimeConstantReactance.xs'})
