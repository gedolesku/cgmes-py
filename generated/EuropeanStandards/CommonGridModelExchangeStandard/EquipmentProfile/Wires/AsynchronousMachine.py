from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.Frequency import Frequency
from ...DomainProfile.Integer import Integer
from ...DomainProfile.PerCent import PerCent
from ...DomainProfile.RotationSpeed import RotationSpeed
from ...DomainProfile.Simple_Float import Simple_Float
from .RotatingMachine import RotatingMachine
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class AsynchronousMachine(RotatingMachine):
    converterFedDrive: Boolean = field(metadata={'xpath': 'cim:AsynchronousMachine.converterFedDrive'})
    efficiency: PerCent = field(metadata={'xpath': 'cim:AsynchronousMachine.efficiency'})
    iaIrRatio: Simple_Float = field(metadata={'xpath': 'cim:AsynchronousMachine.iaIrRatio'})
    polePairNumber: Integer = field(metadata={'xpath': 'cim:AsynchronousMachine.polePairNumber'})
    ratedMechanicalPower: ActivePower = field(metadata={'xpath': 'cim:AsynchronousMachine.ratedMechanicalPower'})
    reversible: Boolean = field(metadata={'xpath': 'cim:AsynchronousMachine.reversible'})
    nominalFrequency: Optional[Frequency] = field(default=None, metadata={'xpath': 'cim:AsynchronousMachine.nominalFrequency'})
    nominalSpeed: Optional[RotationSpeed] = field(default=None, metadata={'xpath': 'cim:AsynchronousMachine.nominalSpeed'})
    rxLockedRotorRatio: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:AsynchronousMachine.rxLockedRotorRatio'})
