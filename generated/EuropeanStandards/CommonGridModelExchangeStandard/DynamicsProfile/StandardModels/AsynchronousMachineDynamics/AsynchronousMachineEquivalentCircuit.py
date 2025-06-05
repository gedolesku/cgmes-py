from __future__ import annotations
from ....DomainProfile.PU import PU
from .AsynchronousMachineDynamics import AsynchronousMachineDynamics
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class AsynchronousMachineEquivalentCircuit(AsynchronousMachineDynamics):
    rr1: Optional[PU] = field(default=None, metadata={'xpath': 'cim:AsynchronousMachineEquivalentCircuit.rr1'})
    rr2: Optional[PU] = field(default=None, metadata={'xpath': 'cim:AsynchronousMachineEquivalentCircuit.rr2'})
    xlr1: Optional[PU] = field(default=None, metadata={'xpath': 'cim:AsynchronousMachineEquivalentCircuit.xlr1'})
    xlr2: Optional[PU] = field(default=None, metadata={'xpath': 'cim:AsynchronousMachineEquivalentCircuit.xlr2'})
    xm: Optional[PU] = field(default=None, metadata={'xpath': 'cim:AsynchronousMachineEquivalentCircuit.xm'})
