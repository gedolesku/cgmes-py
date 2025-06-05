from __future__ import annotations
from ..AsynchronousMachineDynamics.AsynchronousMachineDynamics import AsynchronousMachineDynamics
from ..DynamicsFunctionBlock import DynamicsFunctionBlock
from ..SynchronousMachineDynamics.SynchronousMachineDynamics import SynchronousMachineDynamics
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class TurbineGovernorDynamics(DynamicsFunctionBlock, Protocol):
    AsynchronousMachineDynamics_ref: Optional[AsynchronousMachineDynamics]  # metadata: cim='cim:TurbineGovernorDynamics.AsynchronousMachineDynamics', mult='0..1'
    AsynchronousMachineDynamics_id: str
    SynchronousMachineDynamics_ref: list[SynchronousMachineDynamics]  # metadata: cim='cim:TurbineGovernorDynamics.SynchronousMachineDynamics', mult='0..*'
