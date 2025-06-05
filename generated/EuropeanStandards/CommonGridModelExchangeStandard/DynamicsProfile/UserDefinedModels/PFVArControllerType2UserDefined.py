from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.PFVArControllerType2Dynamics.PFVArControllerType2Dynamics import PFVArControllerType2Dynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PFVArControllerType2UserDefined(PFVArControllerType2Dynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:PFVArControllerType2UserDefined.proprietary'})
