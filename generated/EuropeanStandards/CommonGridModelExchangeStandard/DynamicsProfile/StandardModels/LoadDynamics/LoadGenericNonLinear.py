from __future__ import annotations
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from .GenericNonLinearLoadModelKind import GenericNonLinearLoadModelKind
from .LoadDynamics import LoadDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class LoadGenericNonLinear(LoadDynamics):
    bs: Simple_Float = field(metadata={'xpath': 'cim:LoadGenericNonLinear.bs'})
    bt: Simple_Float = field(metadata={'xpath': 'cim:LoadGenericNonLinear.bt'})
    genericNonLinearLoadModelType: GenericNonLinearLoadModelKind = field(metadata={'xpath': 'cim:LoadGenericNonLinear.genericNonLinearLoadModelType'})
    ls: Simple_Float = field(metadata={'xpath': 'cim:LoadGenericNonLinear.ls'})
    lt: Simple_Float = field(metadata={'xpath': 'cim:LoadGenericNonLinear.lt'})
    pt: Simple_Float = field(metadata={'xpath': 'cim:LoadGenericNonLinear.pt'})
    qt: Simple_Float = field(metadata={'xpath': 'cim:LoadGenericNonLinear.qt'})
    tp: Seconds = field(metadata={'xpath': 'cim:LoadGenericNonLinear.tp'})
    tq: Seconds = field(metadata={'xpath': 'cim:LoadGenericNonLinear.tq'})
