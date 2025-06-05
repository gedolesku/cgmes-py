from __future__ import annotations
from ...StateVariablesProfile.Topology.TopologicalNode import TopologicalNode
from ..Core.BaseVoltage import BaseVoltage
from ..Core.ConnectivityNodeContainer import ConnectivityNodeContainer
from ..Core.ReportingGroup import ReportingGroup
from dataclasses import dataclass, field
from typing import Optional, List
# pylint: disable=function-redefined

@dataclass(kw_only=True)
class TopologicalNode(TopologicalNode):
    BaseVoltage_id: str | None = field(default=None, metadata={"xpath": "cim:TopologicalNode.BaseVoltage/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    BaseVoltage_ref: BaseVoltage = None
    ConnectivityNodeContainer_id: str | None = field(default=None, metadata={"xpath": "cim:TopologicalNode.ConnectivityNodeContainer/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    ConnectivityNodeContainer_ref: ConnectivityNodeContainer = None
    ReportingGroup_id: str | None = field(default=None, metadata={"xpath": "cim:TopologicalNode.ReportingGroup/@rdf:resource", "pattern": r"^#.+$"})
    ReportingGroup_ref: ReportingGroup | None = None
