from __future__ import annotations
from ..AsynchronousMachineDynamics.AsynchronousMachineDynamics import AsynchronousMachineDynamics
from ..DynamicsFunctionBlock import DynamicsFunctionBlock
from ..SynchronousMachineDynamics.SynchronousMachineDynamics import SynchronousMachineDynamics
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class MechanicalLoadDynamics(DynamicsFunctionBlock, Protocol):
    SynchronousMachineDynamics_ref: Optional[SynchronousMachineDynamics]  # metadata: cim='cim:MechanicalLoadDynamics.SynchronousMachineDynamics', mult='0..1'
    SynchronousMachineDynamics_id: str
    AsynchronousMachineDynamics_ref: Optional[AsynchronousMachineDynamics]  # metadata: cim='cim:MechanicalLoadDynamics.AsynchronousMachineDynamics', mult='0..1'
    AsynchronousMachineDynamics_id: str
