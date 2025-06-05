from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .TurbineLoadControllerDynamics import TurbineLoadControllerDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class TurbLCFB1(TurbineLoadControllerDynamics):
    db: PU = field(metadata={'xpath': 'cim:TurbLCFB1.db'})
    emax: PU = field(metadata={'xpath': 'cim:TurbLCFB1.emax'})
    fb: PU = field(metadata={'xpath': 'cim:TurbLCFB1.fb'})
    fbf: Boolean = field(metadata={'xpath': 'cim:TurbLCFB1.fbf'})
    irmax: PU = field(metadata={'xpath': 'cim:TurbLCFB1.irmax'})
    ki: PU = field(metadata={'xpath': 'cim:TurbLCFB1.ki'})
    kp: PU = field(metadata={'xpath': 'cim:TurbLCFB1.kp'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:TurbLCFB1.mwbase'})
    pbf: Boolean = field(metadata={'xpath': 'cim:TurbLCFB1.pbf'})
    pmwset: ActivePower = field(metadata={'xpath': 'cim:TurbLCFB1.pmwset'})
    speedReferenceGovernor: Boolean = field(metadata={'xpath': 'cim:TurbLCFB1.speedReferenceGovernor'})
    tpelec: Seconds = field(metadata={'xpath': 'cim:TurbLCFB1.tpelec'})
