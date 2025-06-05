from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.PFVArControllerType1Dynamics.PFVArControllerType1Dynamics import PFVArControllerType1Dynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PFVArControllerType1UserDefined(PFVArControllerType1Dynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:PFVArControllerType1UserDefined.proprietary'})
