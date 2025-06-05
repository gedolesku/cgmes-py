from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovHydroPID2(TurbineGovernorDynamics):
    atw: PU = field(metadata={'xpath': 'cim:GovHydroPID2.atw'})
    d: PU = field(metadata={'xpath': 'cim:GovHydroPID2.d'})
    feedbackSignal: Boolean = field(metadata={'xpath': 'cim:GovHydroPID2.feedbackSignal'})
    g0: PU = field(metadata={'xpath': 'cim:GovHydroPID2.g0'})
    g1: PU = field(metadata={'xpath': 'cim:GovHydroPID2.g1'})
    g2: PU = field(metadata={'xpath': 'cim:GovHydroPID2.g2'})
    gmax: PU = field(metadata={'xpath': 'cim:GovHydroPID2.gmax'})
    gmin: PU = field(metadata={'xpath': 'cim:GovHydroPID2.gmin'})
    kd: PU = field(metadata={'xpath': 'cim:GovHydroPID2.kd'})
    ki: Simple_Float = field(metadata={'xpath': 'cim:GovHydroPID2.ki'})
    kp: PU = field(metadata={'xpath': 'cim:GovHydroPID2.kp'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovHydroPID2.mwbase'})
    p1: PU = field(metadata={'xpath': 'cim:GovHydroPID2.p1'})
    p2: PU = field(metadata={'xpath': 'cim:GovHydroPID2.p2'})
    p3: PU = field(metadata={'xpath': 'cim:GovHydroPID2.p3'})
    rperm: PU = field(metadata={'xpath': 'cim:GovHydroPID2.rperm'})
    ta: Seconds = field(metadata={'xpath': 'cim:GovHydroPID2.ta'})
    tb: Seconds = field(metadata={'xpath': 'cim:GovHydroPID2.tb'})
    treg: Seconds = field(metadata={'xpath': 'cim:GovHydroPID2.treg'})
    tw: Seconds = field(metadata={'xpath': 'cim:GovHydroPID2.tw'})
    velmax: Simple_Float = field(metadata={'xpath': 'cim:GovHydroPID2.velmax'})
    velmin: Simple_Float = field(metadata={'xpath': 'cim:GovHydroPID2.velmin'})
