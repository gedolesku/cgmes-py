from __future__ import annotations
from ....DomainProfile.Seconds import Seconds
from .VoltageCompensatorDynamics import VoltageCompensatorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class VCompIEEEType2(VoltageCompensatorDynamics):
    tr: Seconds = field(metadata={'xpath': 'cim:VCompIEEEType2.tr'})
