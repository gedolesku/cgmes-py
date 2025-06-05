from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ...DomainProfile.ActivePowerPerFrequency import ActivePowerPerFrequency
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.CurrentFlow import CurrentFlow
from ...DomainProfile.PU import PU
from ...DomainProfile.ReactivePower import ReactivePower
from ...DomainProfile.Simple_Float import Simple_Float
from .RegulatingCondEq import RegulatingCondEq
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class ExternalNetworkInjection(RegulatingCondEq):
    governorSCD: ActivePowerPerFrequency = field(metadata={'xpath': 'cim:ExternalNetworkInjection.governorSCD'})
    maxInitialSymShCCurrent: CurrentFlow = field(metadata={'xpath': 'cim:ExternalNetworkInjection.maxInitialSymShCCurrent'})
    maxP: ActivePower = field(metadata={'xpath': 'cim:ExternalNetworkInjection.maxP'})
    maxQ: ReactivePower = field(metadata={'xpath': 'cim:ExternalNetworkInjection.maxQ'})
    maxR0ToX0Ratio: Simple_Float = field(metadata={'xpath': 'cim:ExternalNetworkInjection.maxR0ToX0Ratio'})
    maxR1ToX1Ratio: Simple_Float = field(metadata={'xpath': 'cim:ExternalNetworkInjection.maxR1ToX1Ratio'})
    maxZ0ToZ1Ratio: Simple_Float = field(metadata={'xpath': 'cim:ExternalNetworkInjection.maxZ0ToZ1Ratio'})
    minInitialSymShCCurrent: CurrentFlow = field(metadata={'xpath': 'cim:ExternalNetworkInjection.minInitialSymShCCurrent'})
    minP: ActivePower = field(metadata={'xpath': 'cim:ExternalNetworkInjection.minP'})
    minQ: ReactivePower = field(metadata={'xpath': 'cim:ExternalNetworkInjection.minQ'})
    minR0ToX0Ratio: Simple_Float = field(metadata={'xpath': 'cim:ExternalNetworkInjection.minR0ToX0Ratio'})
    minR1ToX1Ratio: Simple_Float = field(metadata={'xpath': 'cim:ExternalNetworkInjection.minR1ToX1Ratio'})
    minZ0ToZ1Ratio: Simple_Float = field(metadata={'xpath': 'cim:ExternalNetworkInjection.minZ0ToZ1Ratio'})
    ikSecond: Optional[Boolean] = field(default=None, metadata={'xpath': 'cim:ExternalNetworkInjection.ikSecond'})
    voltageFactor: Optional[PU] = field(default=None, metadata={'xpath': 'cim:ExternalNetworkInjection.voltageFactor'})
