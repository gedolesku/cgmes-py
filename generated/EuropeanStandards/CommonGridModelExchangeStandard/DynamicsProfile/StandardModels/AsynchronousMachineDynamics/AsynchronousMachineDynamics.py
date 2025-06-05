from __future__ import annotations
from ...Wires.AsynchronousMachine import AsynchronousMachine
from ..RotatingMachineDynamics import RotatingMachineDynamics
from typing import Protocol, runtime_checkable

@runtime_checkable
class AsynchronousMachineDynamics(RotatingMachineDynamics, Protocol):
    AsynchronousMachine_ref: AsynchronousMachine  # metadata: cim='cim:AsynchronousMachineDynamics.AsynchronousMachine', mult='1'
    AsynchronousMachine_id: str
