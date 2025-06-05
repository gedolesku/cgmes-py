from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.VoltageAdjusterDynamics.VoltageAdjusterDynamics import VoltageAdjusterDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class VoltageAdjusterUserDefined(VoltageAdjusterDynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:VoltageAdjusterUserDefined.proprietary'})
