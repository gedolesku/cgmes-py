from __future__ import annotations
from ....DomainProfile.PU import PU
from .SynchronousMachineDetailed import SynchronousMachineDetailed
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class SynchronousMachineEquivalentCircuit(SynchronousMachineDetailed):
    r1d: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineEquivalentCircuit.r1d'})
    r1q: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineEquivalentCircuit.r1q'})
    r2q: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineEquivalentCircuit.r2q'})
    rfd: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineEquivalentCircuit.rfd'})
    x1d: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineEquivalentCircuit.x1d'})
    x1q: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineEquivalentCircuit.x1q'})
    x2q: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineEquivalentCircuit.x2q'})
    xad: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineEquivalentCircuit.xad'})
    xaq: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineEquivalentCircuit.xaq'})
    xf1d: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineEquivalentCircuit.xf1d'})
    xfd: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineEquivalentCircuit.xfd'})
