from __future__ import annotations
from ..DomainProfile.Date import Date
from ..DomainProfile.String import String
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class StateVariablesVersion(Protocol):
    baseUML: String  # metadata: cim='cim:StateVariablesVersion.baseUML', mult='1'
    baseURI: String  # metadata: cim='cim:StateVariablesVersion.baseURI', mult='1'
    differenceModelURI: String  # metadata: cim='cim:StateVariablesVersion.differenceModelURI', mult='1'
    entsoeUML: String  # metadata: cim='cim:StateVariablesVersion.entsoeUML', mult='1'
    entsoeURI: String  # metadata: cim='cim:StateVariablesVersion.entsoeURI', mult='1'
    modelDescriptionURI: String  # metadata: cim='cim:StateVariablesVersion.modelDescriptionURI', mult='1'
    namespaceRDF: String  # metadata: cim='cim:StateVariablesVersion.namespaceRDF', mult='1'
    namespaceUML: String  # metadata: cim='cim:StateVariablesVersion.namespaceUML', mult='1'
    shortName: String  # metadata: cim='cim:StateVariablesVersion.shortName', mult='1'
    date: Optional[Date]  # metadata: cim='cim:StateVariablesVersion.date', mult='0..1'
