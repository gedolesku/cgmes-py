from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ...DomainProfile.Integer import Integer
from ...DomainProfile.ReactivePower import ReactivePower
from .RegulatingCondEq import RegulatingCondEq
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ExternalNetworkInjection(RegulatingCondEq):
    p: ActivePower = field(metadata={'xpath': 'cim:ExternalNetworkInjection.p'})
    q: ReactivePower = field(metadata={'xpath': 'cim:ExternalNetworkInjection.q'})
    referencePriority: Integer = field(metadata={'xpath': 'cim:ExternalNetworkInjection.referencePriority'})
