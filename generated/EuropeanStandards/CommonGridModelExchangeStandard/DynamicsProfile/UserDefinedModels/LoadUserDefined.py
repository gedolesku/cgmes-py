from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.LoadDynamics.LoadDynamics import LoadDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class LoadUserDefined(LoadDynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:LoadUserDefined.proprietary'})
