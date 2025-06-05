from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ...Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindProtectionIEC(IdentifiedObject):
    fover: PU = field(metadata={'xpath': 'cim:WindProtectionIEC.fover'})
    funder: PU = field(metadata={'xpath': 'cim:WindProtectionIEC.funder'})
    tfover: Seconds = field(metadata={'xpath': 'cim:WindProtectionIEC.tfover'})
    tfunder: Seconds = field(metadata={'xpath': 'cim:WindProtectionIEC.tfunder'})
    tuover: Seconds = field(metadata={'xpath': 'cim:WindProtectionIEC.tuover'})
    tuunder: Seconds = field(metadata={'xpath': 'cim:WindProtectionIEC.tuunder'})
    uover: PU = field(metadata={'xpath': 'cim:WindProtectionIEC.uover'})
    uunder: PU = field(metadata={'xpath': 'cim:WindProtectionIEC.uunder'})
