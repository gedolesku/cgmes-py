from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .VoltageCompensatorDynamics import VoltageCompensatorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class VCompIEEEType1(VoltageCompensatorDynamics):
    rc: PU = field(metadata={'xpath': 'cim:VCompIEEEType1.rc'})
    tr: Seconds = field(metadata={'xpath': 'cim:VCompIEEEType1.tr'})
    xc: PU = field(metadata={'xpath': 'cim:VCompIEEEType1.xc'})
