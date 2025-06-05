from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .RotorKind import RotorKind
from .SynchronousMachineDetailed import SynchronousMachineDetailed
from .SynchronousMachineModelKind import SynchronousMachineModelKind
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class SynchronousMachineTimeConstantReactance(SynchronousMachineDetailed):
    modelType: SynchronousMachineModelKind = field(metadata={'xpath': 'cim:SynchronousMachineTimeConstantReactance.modelType'})
    rotorType: RotorKind = field(metadata={'xpath': 'cim:SynchronousMachineTimeConstantReactance.rotorType'})
    ks: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineTimeConstantReactance.ks'})
    tc: Optional[Seconds] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineTimeConstantReactance.tc'})
    tpdo: Optional[Seconds] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineTimeConstantReactance.tpdo'})
    tppdo: Optional[Seconds] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineTimeConstantReactance.tppdo'})
    tppqo: Optional[Seconds] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineTimeConstantReactance.tppqo'})
    tpqo: Optional[Seconds] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineTimeConstantReactance.tpqo'})
    xDirectSubtrans: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineTimeConstantReactance.xDirectSubtrans'})
    xDirectSync: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineTimeConstantReactance.xDirectSync'})
    xDirectTrans: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineTimeConstantReactance.xDirectTrans'})
    xQuadSubtrans: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineTimeConstantReactance.xQuadSubtrans'})
    xQuadSync: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineTimeConstantReactance.xQuadSync'})
    xQuadTrans: Optional[PU] = field(default=None, metadata={'xpath': 'cim:SynchronousMachineTimeConstantReactance.xQuadTrans'})
