from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from ....DomainProfile.Temperature import Temperature
from .TurbineGovernorDynamics import TurbineGovernorDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GovGAST3(TurbineGovernorDynamics):
    bca: Simple_Float = field(metadata={'xpath': 'cim:GovGAST3.bca'})
    bp: PU = field(metadata={'xpath': 'cim:GovGAST3.bp'})
    dtc: Temperature = field(metadata={'xpath': 'cim:GovGAST3.dtc'})
    ka: PU = field(metadata={'xpath': 'cim:GovGAST3.ka'})
    kac: Simple_Float = field(metadata={'xpath': 'cim:GovGAST3.kac'})
    kca: Simple_Float = field(metadata={'xpath': 'cim:GovGAST3.kca'})
    ksi: Simple_Float = field(metadata={'xpath': 'cim:GovGAST3.ksi'})
    ky: Simple_Float = field(metadata={'xpath': 'cim:GovGAST3.ky'})
    mnef: PU = field(metadata={'xpath': 'cim:GovGAST3.mnef'})
    mxef: PU = field(metadata={'xpath': 'cim:GovGAST3.mxef'})
    rcmn: PU = field(metadata={'xpath': 'cim:GovGAST3.rcmn'})
    rcmx: PU = field(metadata={'xpath': 'cim:GovGAST3.rcmx'})
    tac: Seconds = field(metadata={'xpath': 'cim:GovGAST3.tac'})
    tc: Seconds = field(metadata={'xpath': 'cim:GovGAST3.tc'})
    td: Seconds = field(metadata={'xpath': 'cim:GovGAST3.td'})
    tfen: Temperature = field(metadata={'xpath': 'cim:GovGAST3.tfen'})
    tg: Seconds = field(metadata={'xpath': 'cim:GovGAST3.tg'})
    tsi: Seconds = field(metadata={'xpath': 'cim:GovGAST3.tsi'})
    tt: Temperature = field(metadata={'xpath': 'cim:GovGAST3.tt'})
    ttc: Seconds = field(metadata={'xpath': 'cim:GovGAST3.ttc'})
    ty: Seconds = field(metadata={'xpath': 'cim:GovGAST3.ty'})
