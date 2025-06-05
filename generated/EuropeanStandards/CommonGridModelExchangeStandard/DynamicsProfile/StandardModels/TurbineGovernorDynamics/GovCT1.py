from __future__ import annotations
from ....DomainProfile.ActivePower import ActivePower
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .DroopSignalFeedbackKind import DroopSignalFeedbackKind
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovCT1(TurbineGovernorDynamics):
    aset: Simple_Float = field(metadata={'xpath': 'cim:GovCT1.aset'})
    db: PU = field(metadata={'xpath': 'cim:GovCT1.db'})
    dm: PU = field(metadata={'xpath': 'cim:GovCT1.dm'})
    ka: PU = field(metadata={'xpath': 'cim:GovCT1.ka'})
    kdgov: PU = field(metadata={'xpath': 'cim:GovCT1.kdgov'})
    kigov: PU = field(metadata={'xpath': 'cim:GovCT1.kigov'})
    kiload: PU = field(metadata={'xpath': 'cim:GovCT1.kiload'})
    kimw: PU = field(metadata={'xpath': 'cim:GovCT1.kimw'})
    kpgov: PU = field(metadata={'xpath': 'cim:GovCT1.kpgov'})
    kpload: PU = field(metadata={'xpath': 'cim:GovCT1.kpload'})
    kturb: PU = field(metadata={'xpath': 'cim:GovCT1.kturb'})
    ldref: PU = field(metadata={'xpath': 'cim:GovCT1.ldref'})
    maxerr: PU = field(metadata={'xpath': 'cim:GovCT1.maxerr'})
    minerr: PU = field(metadata={'xpath': 'cim:GovCT1.minerr'})
    mwbase: ActivePower = field(metadata={'xpath': 'cim:GovCT1.mwbase'})
    r: PU = field(metadata={'xpath': 'cim:GovCT1.r'})
    rclose: Simple_Float = field(metadata={'xpath': 'cim:GovCT1.rclose'})
    rdown: PU = field(metadata={'xpath': 'cim:GovCT1.rdown'})
    ropen: Simple_Float = field(metadata={'xpath': 'cim:GovCT1.ropen'})
    rselect: DroopSignalFeedbackKind = field(metadata={'xpath': 'cim:GovCT1.rselect'})
    rup: PU = field(metadata={'xpath': 'cim:GovCT1.rup'})
    ta: Seconds = field(metadata={'xpath': 'cim:GovCT1.ta'})
    tact: Seconds = field(metadata={'xpath': 'cim:GovCT1.tact'})
    tb: Seconds = field(metadata={'xpath': 'cim:GovCT1.tb'})
    tc: Seconds = field(metadata={'xpath': 'cim:GovCT1.tc'})
    tdgov: Seconds = field(metadata={'xpath': 'cim:GovCT1.tdgov'})
    teng: Seconds = field(metadata={'xpath': 'cim:GovCT1.teng'})
    tfload: Seconds = field(metadata={'xpath': 'cim:GovCT1.tfload'})
    tpelec: Seconds = field(metadata={'xpath': 'cim:GovCT1.tpelec'})
    tsa: Seconds = field(metadata={'xpath': 'cim:GovCT1.tsa'})
    tsb: Seconds = field(metadata={'xpath': 'cim:GovCT1.tsb'})
    vmax: PU = field(metadata={'xpath': 'cim:GovCT1.vmax'})
    vmin: PU = field(metadata={'xpath': 'cim:GovCT1.vmin'})
    wfnl: PU = field(metadata={'xpath': 'cim:GovCT1.wfnl'})
    wfspd: Boolean = field(metadata={'xpath': 'cim:GovCT1.wfspd'})
