from __future__ import annotations
from ..DomainProfile.Date import Date
from ..DomainProfile.String import String
from typing import Protocol, runtime_checkable

@runtime_checkable
class GeographicalLocationVersion(Protocol):
    baseUML: String  # metadata: cim='cim:GeographicalLocationVersion.baseUML', mult='1'
    baseURI: String  # metadata: cim='cim:GeographicalLocationVersion.baseURI', mult='1'
    date: Date  # metadata: cim='cim:GeographicalLocationVersion.date', mult='1'
    differenceModelURI: String  # metadata: cim='cim:GeographicalLocationVersion.differenceModelURI', mult='1'
    entsoeUML: String  # metadata: cim='cim:GeographicalLocationVersion.entsoeUML', mult='1'
    entsoeURI: String  # metadata: cim='cim:GeographicalLocationVersion.entsoeURI', mult='1'
    modelDescriptionURI: String  # metadata: cim='cim:GeographicalLocationVersion.modelDescriptionURI', mult='1'
    namespaceRDF: String  # metadata: cim='cim:GeographicalLocationVersion.namespaceRDF', mult='1'
    namespaceUML: String  # metadata: cim='cim:GeographicalLocationVersion.namespaceUML', mult='1'
    shortName: String  # metadata: cim='cim:GeographicalLocationVersion.shortName', mult='1'
