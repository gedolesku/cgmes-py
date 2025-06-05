from __future__ import annotations
from ..DomainProfile.Date import Date
from ..DomainProfile.String import String
from typing import Protocol, runtime_checkable

@runtime_checkable
class SteadyStateHypothesisVersion(Protocol):
    baseUML: String  # metadata: cim='cim:SteadyStateHypothesisVersion.baseUML', mult='1'
    baseURI: String  # metadata: cim='cim:SteadyStateHypothesisVersion.baseURI', mult='1'
    date: Date  # metadata: cim='cim:SteadyStateHypothesisVersion.date', mult='1'
    differenceModelURI: String  # metadata: cim='cim:SteadyStateHypothesisVersion.differenceModelURI', mult='1'
    entsoeUML: String  # metadata: cim='cim:SteadyStateHypothesisVersion.entsoeUML', mult='1'
    entsoeURI: String  # metadata: cim='cim:SteadyStateHypothesisVersion.entsoeURI', mult='1'
    modelDescriptionURI: String  # metadata: cim='cim:SteadyStateHypothesisVersion.modelDescriptionURI', mult='1'
    namespaceRDF: String  # metadata: cim='cim:SteadyStateHypothesisVersion.namespaceRDF', mult='1'
    namespaceUML: String  # metadata: cim='cim:SteadyStateHypothesisVersion.namespaceUML', mult='1'
    shortName: String  # metadata: cim='cim:SteadyStateHypothesisVersion.shortName', mult='1'
