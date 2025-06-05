from __future__ import annotations
from ..DynamicsFunctionBlock import DynamicsFunctionBlock
from ..SynchronousMachineDynamics.SynchronousMachineDynamics import SynchronousMachineDynamics
from typing import Protocol, runtime_checkable

@runtime_checkable
class ExcitationSystemDynamics(DynamicsFunctionBlock, Protocol):
    SynchronousMachineDynamics_ref: SynchronousMachineDynamics  # metadata: cim='cim:ExcitationSystemDynamics.SynchronousMachineDynamics', mult='1'
    SynchronousMachineDynamics_id: str
