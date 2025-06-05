from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class DiscExcContIEEEDEC2A(DiscontinuousExcitationControlDynamics):
    td1: Seconds = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC2A.td1'})
    td2: Seconds = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC2A.td2'})
    vdmax: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC2A.vdmax'})
    vdmin: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC2A.vdmin'})
    vk: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC2A.vk'})
