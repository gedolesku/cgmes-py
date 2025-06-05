from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.WindDynamics.WindPlantDynamics import WindPlantDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindPlantUserDefined(WindPlantDynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:WindPlantUserDefined.proprietary'})
