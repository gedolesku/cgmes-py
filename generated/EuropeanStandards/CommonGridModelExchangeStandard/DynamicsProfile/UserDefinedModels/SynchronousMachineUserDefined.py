from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.SynchronousMachineDynamics.SynchronousMachineDynamics import SynchronousMachineDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class SynchronousMachineUserDefined(SynchronousMachineDynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:SynchronousMachineUserDefined.proprietary'})
