from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.VoltageCompensatorDynamics.VoltageCompensatorDynamics import VoltageCompensatorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class VoltageCompensatorUserDefined(VoltageCompensatorDynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:VoltageCompensatorUserDefined.proprietary'})
