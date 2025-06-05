from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .WindGenTurbineType3IEC import WindGenTurbineType3IEC
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindGenTurbineType3bIEC(WindGenTurbineType3IEC):
    fducw: Simple_Float = field(metadata={'xpath': 'cim:WindGenTurbineType3bIEC.fducw'})
    mwtcwp: Boolean = field(metadata={'xpath': 'cim:WindGenTurbineType3bIEC.mwtcwp'})
    tg: Seconds = field(metadata={'xpath': 'cim:WindGenTurbineType3bIEC.tg'})
    two: Seconds = field(metadata={'xpath': 'cim:WindGenTurbineType3bIEC.two'})
    xs: PU = field(metadata={'xpath': 'cim:WindGenTurbineType3bIEC.xs'})
