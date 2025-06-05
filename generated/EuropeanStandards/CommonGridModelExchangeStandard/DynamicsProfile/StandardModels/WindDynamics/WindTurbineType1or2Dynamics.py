from __future__ import annotations
from ...StandardInterconnections.RemoteInputSignal import RemoteInputSignal
from ..AsynchronousMachineDynamics.AsynchronousMachineDynamics import AsynchronousMachineDynamics
from ..DynamicsFunctionBlock import DynamicsFunctionBlock
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class WindTurbineType1or2Dynamics(DynamicsFunctionBlock, Protocol):
    AsynchronousMachineDynamics_ref: AsynchronousMachineDynamics  # metadata: cim='cim:WindTurbineType1or2Dynamics.AsynchronousMachineDynamics', mult='1'
    AsynchronousMachineDynamics_id: str
    RemoteInputSignal_ref: Optional[RemoteInputSignal]  # metadata: cim='cim:WindTurbineType1or2Dynamics.RemoteInputSignal', mult='0..1'
    RemoteInputSignal_id: str
