from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PowerSystemStabilizerUserDefined(PowerSystemStabilizerDynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:PowerSystemStabilizerUserDefined.proprietary'})
