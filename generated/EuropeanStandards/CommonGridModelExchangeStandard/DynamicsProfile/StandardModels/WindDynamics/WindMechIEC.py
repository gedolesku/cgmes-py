from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ...Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindMechIEC(IdentifiedObject):
    cdrt: PU = field(metadata={'xpath': 'cim:WindMechIEC.cdrt'})
    hgen: Seconds = field(metadata={'xpath': 'cim:WindMechIEC.hgen'})
    hwtr: Seconds = field(metadata={'xpath': 'cim:WindMechIEC.hwtr'})
    kdrt: PU = field(metadata={'xpath': 'cim:WindMechIEC.kdrt'})
