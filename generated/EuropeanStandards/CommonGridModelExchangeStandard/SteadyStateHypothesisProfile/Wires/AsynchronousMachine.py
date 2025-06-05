from __future__ import annotations
from .AsynchronousMachineKind import AsynchronousMachineKind
from .RotatingMachine import RotatingMachine
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class AsynchronousMachine(RotatingMachine):
    asynchronousMachineType: AsynchronousMachineKind = field(metadata={'xpath': 'cim:AsynchronousMachine.asynchronousMachineType'})
