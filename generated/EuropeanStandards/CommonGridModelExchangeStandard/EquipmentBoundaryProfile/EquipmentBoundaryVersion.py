from __future__ import annotations
from ..DomainProfile.Date import Date
from ..DomainProfile.String import String
from typing import Protocol, runtime_checkable

@runtime_checkable
class EquipmentBoundaryVersion(Protocol):
    baseUML: String  # metadata: cim='cim:EquipmentBoundaryVersion.baseUML', mult='1'
    baseURI: String  # metadata: cim='cim:EquipmentBoundaryVersion.baseURI', mult='1'
    date: Date  # metadata: cim='cim:EquipmentBoundaryVersion.date', mult='1'
    differenceModelURI: String  # metadata: cim='cim:EquipmentBoundaryVersion.differenceModelURI', mult='1'
    entsoeUML: String  # metadata: cim='cim:EquipmentBoundaryVersion.entsoeUML', mult='1'
    entsoeURIcore: String  # metadata: cim='cim:EquipmentBoundaryVersion.entsoeURIcore', mult='1'
    entsoeURIoperation: String  # metadata: cim='cim:EquipmentBoundaryVersion.entsoeURIoperation', mult='1'
    modelDescriptionURI: String  # metadata: cim='cim:EquipmentBoundaryVersion.modelDescriptionURI', mult='1'
    namespaceRDF: String  # metadata: cim='cim:EquipmentBoundaryVersion.namespaceRDF', mult='1'
    namespaceUML: String  # metadata: cim='cim:EquipmentBoundaryVersion.namespaceUML', mult='1'
    shortName: String  # metadata: cim='cim:EquipmentBoundaryVersion.shortName', mult='1'
