from __future__ import annotations
from ..DomainProfile.Date import Date
from ..DomainProfile.String import String
from typing import Protocol, runtime_checkable

@runtime_checkable
class TopologyBoundaryVersion(Protocol):
    baseUML: String  # metadata: cim='cim:TopologyBoundaryVersion.baseUML', mult='1'
    baseURI: String  # metadata: cim='cim:TopologyBoundaryVersion.baseURI', mult='1'
    date: Date  # metadata: cim='cim:TopologyBoundaryVersion.date', mult='1'
    differenceModelURI: String  # metadata: cim='cim:TopologyBoundaryVersion.differenceModelURI', mult='1'
    entsoeUML: String  # metadata: cim='cim:TopologyBoundaryVersion.entsoeUML', mult='1'
    entsoeURI: String  # metadata: cim='cim:TopologyBoundaryVersion.entsoeURI', mult='1'
    modelDescriptionURI: String  # metadata: cim='cim:TopologyBoundaryVersion.modelDescriptionURI', mult='1'
    namespaceRDF: String  # metadata: cim='cim:TopologyBoundaryVersion.namespaceRDF', mult='1'
    namespaceUML: String  # metadata: cim='cim:TopologyBoundaryVersion.namespaceUML', mult='1'
    shortName: String  # metadata: cim='cim:TopologyBoundaryVersion.shortName', mult='1'
