from __future__ import annotations
from ..DomainProfile.Date import Date
from ..DomainProfile.String import String
from typing import Protocol, runtime_checkable

@runtime_checkable
class EquipmentVersion(Protocol):
    baseUML: String  # metadata: cim='cim:EquipmentVersion.baseUML', mult='1'
    baseURIcore: String  # metadata: cim='cim:EquipmentVersion.baseURIcore', mult='1'
    baseURIoperation: String  # metadata: cim='cim:EquipmentVersion.baseURIoperation', mult='1'
    baseURIshortCircuit: String  # metadata: cim='cim:EquipmentVersion.baseURIshortCircuit', mult='1'
    date: Date  # metadata: cim='cim:EquipmentVersion.date', mult='1'
    differenceModelURI: String  # metadata: cim='cim:EquipmentVersion.differenceModelURI', mult='1'
    entsoeUML: String  # metadata: cim='cim:EquipmentVersion.entsoeUML', mult='1'
    entsoeURIcore: String  # metadata: cim='cim:EquipmentVersion.entsoeURIcore', mult='1'
    entsoeURIoperation: String  # metadata: cim='cim:EquipmentVersion.entsoeURIoperation', mult='1'
    entsoeURIshortCircuit: String  # metadata: cim='cim:EquipmentVersion.entsoeURIshortCircuit', mult='1'
    modelDescriptionURI: String  # metadata: cim='cim:EquipmentVersion.modelDescriptionURI', mult='1'
    namespaceRDF: String  # metadata: cim='cim:EquipmentVersion.namespaceRDF', mult='1'
    namespaceUML: String  # metadata: cim='cim:EquipmentVersion.namespaceUML', mult='1'
    shortName: String  # metadata: cim='cim:EquipmentVersion.shortName', mult='1'
