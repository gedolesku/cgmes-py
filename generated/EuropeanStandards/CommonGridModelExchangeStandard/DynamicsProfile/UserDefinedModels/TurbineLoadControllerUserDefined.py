from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.TurbineLoadControllerDynamics.TurbineLoadControllerDynamics import TurbineLoadControllerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class TurbineLoadControllerUserDefined(TurbineLoadControllerDynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:TurbineLoadControllerUserDefined.proprietary'})
