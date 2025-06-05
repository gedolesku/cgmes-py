from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.String import String
from .ConnectivityNodeContainer import ConnectivityNodeContainer
from .IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ConnectivityNode(IdentifiedObject):
    boundaryPoint: Boolean = field(metadata={'xpath': 'cim:ConnectivityNode.boundaryPoint'})
    fromEndIsoCode: String = field(metadata={'xpath': 'cim:ConnectivityNode.fromEndIsoCode'})
    fromEndName: String = field(metadata={'xpath': 'cim:ConnectivityNode.fromEndName'})
    fromEndNameTso: String = field(metadata={'xpath': 'cim:ConnectivityNode.fromEndNameTso'})
    toEndIsoCode: String = field(metadata={'xpath': 'cim:ConnectivityNode.toEndIsoCode'})
    toEndName: String = field(metadata={'xpath': 'cim:ConnectivityNode.toEndName'})
    toEndNameTso: String = field(metadata={'xpath': 'cim:ConnectivityNode.toEndNameTso'})
    ConnectivityNodeContainer_id: str | None = field(default=None, metadata={"xpath": "cim:ConnectivityNode.ConnectivityNodeContainer/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    ConnectivityNodeContainer_ref: ConnectivityNodeContainer = None
