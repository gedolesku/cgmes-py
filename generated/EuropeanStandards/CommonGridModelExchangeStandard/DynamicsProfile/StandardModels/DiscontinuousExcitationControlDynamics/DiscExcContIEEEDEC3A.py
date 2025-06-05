from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class DiscExcContIEEEDEC3A(DiscontinuousExcitationControlDynamics):
    tdr: Seconds = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC3A.tdr'})
    vtmin: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC3A.vtmin'})
