from __future__ import annotations
from ....DomainProfile.Simple_Float import Simple_Float
from ...Core.IdentifiedObject import IdentifiedObject
from .LoadAggregate import LoadAggregate
from .StaticLoadModelKind import StaticLoadModelKind
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class LoadStatic(IdentifiedObject):
    staticLoadModelType: StaticLoadModelKind = field(metadata={'xpath': 'cim:LoadStatic.staticLoadModelType'})
    LoadAggregate_id: str | None = field(default=None, metadata={"xpath": "cim:LoadStatic.LoadAggregate/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    LoadAggregate_ref: LoadAggregate = None
    ep1: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.ep1'})
    ep2: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.ep2'})
    ep3: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.ep3'})
    eq1: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.eq1'})
    eq2: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.eq2'})
    eq3: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.eq3'})
    kp1: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.kp1'})
    kp2: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.kp2'})
    kp3: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.kp3'})
    kp4: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.kp4'})
    kpf: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.kpf'})
    kq1: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.kq1'})
    kq2: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.kq2'})
    kq3: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.kq3'})
    kq4: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.kq4'})
    kqf: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadStatic.kqf'})
