from __future__ import annotations
from ....DomainProfile.AngleDegrees import AngleDegrees
from ....DomainProfile.PU import PU
from ...Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindAeroLinearIEC(IdentifiedObject):
    dpomega: PU = field(metadata={'xpath': 'cim:WindAeroLinearIEC.dpomega'})
    dptheta: PU = field(metadata={'xpath': 'cim:WindAeroLinearIEC.dptheta'})
    omegazero: PU = field(metadata={'xpath': 'cim:WindAeroLinearIEC.omegazero'})
    pavail: PU = field(metadata={'xpath': 'cim:WindAeroLinearIEC.pavail'})
    thetazero: AngleDegrees = field(metadata={'xpath': 'cim:WindAeroLinearIEC.thetazero'})
