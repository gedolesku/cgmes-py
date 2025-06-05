from __future__ import annotations
from ..DomainProfile.Date import Date
from ..DomainProfile.String import String
from typing import Protocol, runtime_checkable

@runtime_checkable
class DiagramLayoutVersion(Protocol):
    baseUML: String  # metadata: cim='cim:DiagramLayoutVersion.baseUML', mult='1'
    baseURI: String  # metadata: cim='cim:DiagramLayoutVersion.baseURI', mult='1'
    date: Date  # metadata: cim='cim:DiagramLayoutVersion.date', mult='1'
    differenceModelURI: String  # metadata: cim='cim:DiagramLayoutVersion.differenceModelURI', mult='1'
    entsoeUML: String  # metadata: cim='cim:DiagramLayoutVersion.entsoeUML', mult='1'
    entsoeURI: String  # metadata: cim='cim:DiagramLayoutVersion.entsoeURI', mult='1'
    modelDescriptionURI: String  # metadata: cim='cim:DiagramLayoutVersion.modelDescriptionURI', mult='1'
    namespaceRDF: String  # metadata: cim='cim:DiagramLayoutVersion.namespaceRDF', mult='1'
    namespaceUML: String  # metadata: cim='cim:DiagramLayoutVersion.namespaceUML', mult='1'
    shortName: String  # metadata: cim='cim:DiagramLayoutVersion.shortName', mult='1'
