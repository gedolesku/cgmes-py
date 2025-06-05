from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ...DomainProfile.ReactivePower import ReactivePower
from ..Topology.TopologicalNode import TopologicalNode
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class SvInjection:
    pInjection: ActivePower = field(metadata={'xpath': 'cim:SvInjection.pInjection'})
    TopologicalNode_id: str | None = field(default=None, metadata={"xpath": "cim:SvInjection.TopologicalNode/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    TopologicalNode_ref: TopologicalNode = None
    qInjection: Optional[ReactivePower] = field(default=None, metadata={'xpath': 'cim:SvInjection.qInjection'})
