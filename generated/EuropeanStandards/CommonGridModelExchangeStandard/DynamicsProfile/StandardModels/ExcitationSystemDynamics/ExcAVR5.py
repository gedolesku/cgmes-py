from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .ExcitationSystemDynamics import ExcitationSystemDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExcAVR5(ExcitationSystemDynamics):
    ka: PU = field(metadata={'xpath': 'cim:ExcAVR5.ka'})
    rex: PU = field(metadata={'xpath': 'cim:ExcAVR5.rex'})
    ta: Seconds = field(metadata={'xpath': 'cim:ExcAVR5.ta'})
