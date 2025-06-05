from __future__ import annotations
from ..DomainProfile.Date import Date
from ..DomainProfile.String import String
from typing import Protocol, runtime_checkable

@runtime_checkable
class DynamicsVersion(Protocol):
    baseUML: String  # metadata: cim='cim:DynamicsVersion.baseUML', mult='1'
    baseURI: String  # metadata: cim='cim:DynamicsVersion.baseURI', mult='1'
    date: Date  # metadata: cim='cim:DynamicsVersion.date', mult='1'
    differenceModelURI: String  # metadata: cim='cim:DynamicsVersion.differenceModelURI', mult='1'
    entsoeUML: String  # metadata: cim='cim:DynamicsVersion.entsoeUML', mult='1'
    entsoeURI: String  # metadata: cim='cim:DynamicsVersion.entsoeURI', mult='1'
    modelDescriptionURI: String  # metadata: cim='cim:DynamicsVersion.modelDescriptionURI', mult='1'
    namespaceRDF: String  # metadata: cim='cim:DynamicsVersion.namespaceRDF', mult='1'
    namespaceUML: String  # metadata: cim='cim:DynamicsVersion.namespaceUML', mult='1'
    shortName: String  # metadata: cim='cim:DynamicsVersion.shortName', mult='1'
