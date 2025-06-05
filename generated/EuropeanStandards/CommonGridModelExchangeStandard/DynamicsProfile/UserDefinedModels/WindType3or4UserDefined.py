from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ..StandardModels.WindDynamics.WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindType3or4UserDefined(WindTurbineType3or4Dynamics):
    proprietary: Boolean = field(metadata={'xpath': 'cim:WindType3or4UserDefined.proprietary'})
