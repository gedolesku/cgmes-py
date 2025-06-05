from __future__ import annotations
from ....DomainProfile.AngleDegrees import AngleDegrees
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from ...Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindContPitchAngleIEC(IdentifiedObject):
    dthetamax: Simple_Float = field(metadata={'xpath': 'cim:WindContPitchAngleIEC.dthetamax'})
    dthetamin: Simple_Float = field(metadata={'xpath': 'cim:WindContPitchAngleIEC.dthetamin'})
    kic: PU = field(metadata={'xpath': 'cim:WindContPitchAngleIEC.kic'})
    kiomega: PU = field(metadata={'xpath': 'cim:WindContPitchAngleIEC.kiomega'})
    kpc: PU = field(metadata={'xpath': 'cim:WindContPitchAngleIEC.kpc'})
    kpomega: PU = field(metadata={'xpath': 'cim:WindContPitchAngleIEC.kpomega'})
    kpx: PU = field(metadata={'xpath': 'cim:WindContPitchAngleIEC.kpx'})
    thetamax: AngleDegrees = field(metadata={'xpath': 'cim:WindContPitchAngleIEC.thetamax'})
    thetamin: AngleDegrees = field(metadata={'xpath': 'cim:WindContPitchAngleIEC.thetamin'})
    ttheta: Seconds = field(metadata={'xpath': 'cim:WindContPitchAngleIEC.ttheta'})
