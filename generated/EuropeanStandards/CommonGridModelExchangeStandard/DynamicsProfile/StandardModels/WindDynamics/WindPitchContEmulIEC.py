from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from ...Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindPitchContEmulIEC(IdentifiedObject):
    kdroop: Simple_Float = field(metadata={'xpath': 'cim:WindPitchContEmulIEC.kdroop'})
    kipce: Simple_Float = field(metadata={'xpath': 'cim:WindPitchContEmulIEC.kipce'})
    komegaaero: PU = field(metadata={'xpath': 'cim:WindPitchContEmulIEC.komegaaero'})
    kppce: Simple_Float = field(metadata={'xpath': 'cim:WindPitchContEmulIEC.kppce'})
    omegaref: PU = field(metadata={'xpath': 'cim:WindPitchContEmulIEC.omegaref'})
    pimax: PU = field(metadata={'xpath': 'cim:WindPitchContEmulIEC.pimax'})
    pimin: PU = field(metadata={'xpath': 'cim:WindPitchContEmulIEC.pimin'})
    t1: Seconds = field(metadata={'xpath': 'cim:WindPitchContEmulIEC.t1'})
    t2: Seconds = field(metadata={'xpath': 'cim:WindPitchContEmulIEC.t2'})
    tpe: Seconds = field(metadata={'xpath': 'cim:WindPitchContEmulIEC.tpe'})
