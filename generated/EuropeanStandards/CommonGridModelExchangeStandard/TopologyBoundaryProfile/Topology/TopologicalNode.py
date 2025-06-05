from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.String import String
from ..Core.BaseVoltage import BaseVoltage
from ..Core.ConnectivityNodeContainer import ConnectivityNodeContainer
from ..Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class TopologicalNode(IdentifiedObject):
    boundaryPoint: Boolean = field(metadata={'xpath': 'cim:TopologicalNode.boundaryPoint'})
    fromEndIsoCode: String = field(metadata={'xpath': 'cim:TopologicalNode.fromEndIsoCode'})
    fromEndName: String = field(metadata={'xpath': 'cim:TopologicalNode.fromEndName'})
    fromEndNameTso: String = field(metadata={'xpath': 'cim:TopologicalNode.fromEndNameTso'})
    toEndIsoCode: String = field(metadata={'xpath': 'cim:TopologicalNode.toEndIsoCode'})
    toEndName: String = field(metadata={'xpath': 'cim:TopologicalNode.toEndName'})
    toEndNameTso: String = field(metadata={'xpath': 'cim:TopologicalNode.toEndNameTso'})
    ConnectivityNodeContainer_id: str | None = field(default=None, metadata={"xpath": "cim:TopologicalNode.ConnectivityNodeContainer/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    ConnectivityNodeContainer_ref: ConnectivityNodeContainer = None
    BaseVoltage_id: str | None = field(default=None, metadata={"xpath": "cim:TopologicalNode.BaseVoltage/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    BaseVoltage_ref: BaseVoltage = None
