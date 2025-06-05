from __future__ import annotations
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .LoadDynamics import LoadDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class LoadComposite(LoadDynamics):
    epfd: Simple_Float = field(metadata={'xpath': 'cim:LoadComposite.epfd'})
    epfs: Simple_Float = field(metadata={'xpath': 'cim:LoadComposite.epfs'})
    epvd: Simple_Float = field(metadata={'xpath': 'cim:LoadComposite.epvd'})
    epvs: Simple_Float = field(metadata={'xpath': 'cim:LoadComposite.epvs'})
    eqfd: Simple_Float = field(metadata={'xpath': 'cim:LoadComposite.eqfd'})
    eqfs: Simple_Float = field(metadata={'xpath': 'cim:LoadComposite.eqfs'})
    eqvd: Simple_Float = field(metadata={'xpath': 'cim:LoadComposite.eqvd'})
    eqvs: Simple_Float = field(metadata={'xpath': 'cim:LoadComposite.eqvs'})
    h: Seconds = field(metadata={'xpath': 'cim:LoadComposite.h'})
    lfrac: Simple_Float = field(metadata={'xpath': 'cim:LoadComposite.lfrac'})
    pfrac: Simple_Float = field(metadata={'xpath': 'cim:LoadComposite.pfrac'})
