from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovGAST4(TurbineGovernorDynamics):
    bp: PU = field(metadata={'xpath': 'cim:GovGAST4.bp'})
    ktm: PU = field(metadata={'xpath': 'cim:GovGAST4.ktm'})
    mnef: PU = field(metadata={'xpath': 'cim:GovGAST4.mnef'})
    mxef: PU = field(metadata={'xpath': 'cim:GovGAST4.mxef'})
    rymn: PU = field(metadata={'xpath': 'cim:GovGAST4.rymn'})
    rymx: PU = field(metadata={'xpath': 'cim:GovGAST4.rymx'})
    ta: Seconds = field(metadata={'xpath': 'cim:GovGAST4.ta'})
    tc: Seconds = field(metadata={'xpath': 'cim:GovGAST4.tc'})
    tcm: Seconds = field(metadata={'xpath': 'cim:GovGAST4.tcm'})
    tm: Seconds = field(metadata={'xpath': 'cim:GovGAST4.tm'})
    tv: Seconds = field(metadata={'xpath': 'cim:GovGAST4.tv'})
