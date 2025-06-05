from __future__ import annotations
from ...DomainProfile.Integer import Integer
from .RotatingMachine import RotatingMachine
from .SynchronousMachineOperatingMode import SynchronousMachineOperatingMode
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class SynchronousMachine(RotatingMachine):
    operatingMode: SynchronousMachineOperatingMode = field(metadata={'xpath': 'cim:SynchronousMachine.operatingMode'})
    referencePriority: Integer = field(metadata={'xpath': 'cim:SynchronousMachine.referencePriority'})
