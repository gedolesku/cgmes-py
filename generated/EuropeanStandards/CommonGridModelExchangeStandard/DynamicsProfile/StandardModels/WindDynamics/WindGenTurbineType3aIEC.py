from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .WindGenTurbineType3IEC import WindGenTurbineType3IEC
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindGenTurbineType3aIEC(WindGenTurbineType3IEC):
    kpc: Simple_Float = field(metadata={'xpath': 'cim:WindGenTurbineType3aIEC.kpc'})
    tic: Seconds = field(metadata={'xpath': 'cim:WindGenTurbineType3aIEC.tic'})
    xs: PU = field(metadata={'xpath': 'cim:WindGenTurbineType3aIEC.xs'})
