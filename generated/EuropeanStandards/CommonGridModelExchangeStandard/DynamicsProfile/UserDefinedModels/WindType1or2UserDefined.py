from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.WindDynamics.WindTurbineType1or2Dynamics import WindTurbineType1or2Dynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindType1or2UserDefined(WindTurbineType1or2Dynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:WindType1or2UserDefined.proprietary'})
