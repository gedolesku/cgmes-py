from __future__ import annotations
from ...DomainProfile.AngleDegrees import AngleDegrees
from ...DomainProfile.Voltage import Voltage
from ..Topology.TopologicalNode import TopologicalNode
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class SvVoltage:
    angle: AngleDegrees = field(metadata={'xpath': 'cim:SvVoltage.angle'})
    v: Voltage = field(metadata={'xpath': 'cim:SvVoltage.v'})
    TopologicalNode_id: str | None = field(default=None, metadata={"xpath": "cim:SvVoltage.TopologicalNode/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    TopologicalNode_ref: TopologicalNode = None
