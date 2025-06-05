from __future__ import annotations
from ..DomainProfile.Date import Date
from ..DomainProfile.String import String
from typing import Protocol, runtime_checkable

@runtime_checkable
class TopologyVersion(Protocol):
    baseUML: String  # metadata: cim='cim:TopologyVersion.baseUML', mult='1'
    baseURI: String  # metadata: cim='cim:TopologyVersion.baseURI', mult='1'
    date: Date  # metadata: cim='cim:TopologyVersion.date', mult='1'
    differenceModelURI: String  # metadata: cim='cim:TopologyVersion.differenceModelURI', mult='1'
    entsoeUML: String  # metadata: cim='cim:TopologyVersion.entsoeUML', mult='1'
    entsoeURI: String  # metadata: cim='cim:TopologyVersion.entsoeURI', mult='1'
    modelDescriptionURI: String  # metadata: cim='cim:TopologyVersion.modelDescriptionURI', mult='1'
    namespaceRDF: String  # metadata: cim='cim:TopologyVersion.namespaceRDF', mult='1'
    namespaceUML: String  # metadata: cim='cim:TopologyVersion.namespaceUML', mult='1'
    shortName: String  # metadata: cim='cim:TopologyVersion.shortName', mult='1'
