from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class TurbineGovernorUserDefined(TurbineGovernorDynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:TurbineGovernorUserDefined.proprietary'})
