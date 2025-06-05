from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.AsynchronousMachineDynamics.AsynchronousMachineDynamics import AsynchronousMachineDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class AsynchronousMachineUserDefined(AsynchronousMachineDynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:AsynchronousMachineUserDefined.proprietary'})
