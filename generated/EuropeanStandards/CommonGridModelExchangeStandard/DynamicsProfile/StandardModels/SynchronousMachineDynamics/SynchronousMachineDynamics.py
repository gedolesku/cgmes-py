from __future__ import annotations
from ...Wires.SynchronousMachine import SynchronousMachine
from ..RotatingMachineDynamics import RotatingMachineDynamics
from typing import Protocol, runtime_checkable

@runtime_checkable
class SynchronousMachineDynamics(RotatingMachineDynamics, Protocol):
    SynchronousMachine_ref: SynchronousMachine  # metadata: cim='cim:SynchronousMachineDynamics.SynchronousMachine', mult='1'
    SynchronousMachine_id: str
