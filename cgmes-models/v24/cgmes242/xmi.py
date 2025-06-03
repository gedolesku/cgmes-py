from dataclasses import dataclass, field
from typing import Optional

from cgmes242.abstract import Abstract
from cgmes242.callout import Callout
from cgmes242.cim_is_rdf_about import CimIsRdfAbout
from cgmes242.cimdatatype import Cimdatatype
from cgmes242.compound import Compound
from cgmes242.date_created import DateCreated
from cgmes242.date_modified import DateModified
from cgmes242.description import Description
from cgmes242.deststyle import Deststyle
from cgmes242.documentation_1 import Documentation1
from cgmes242.ea_dst_xref_property import EaDstXrefProperty
from cgmes242.ea_src_xref_property import EaSrcXrefProperty
from cgmes242.ea_type import EaType
from cgmes242.entsoe import Entsoe
from cgmes242.enum import EnumType
from cgmes242.enumeration import Enumeration
from cgmes242.extension import Extension
from cgmes242.guidbased_on import GuidbasedOn
from cgmes242.head_style import HeadStyle
from cgmes242.is_based_on import IsBasedOn
from cgmes242.lb import Lb
from cgmes242.line_style import LineStyle
from cgmes242.linemode import Linemode
from cgmes242.lt import Lt
from cgmes242.model_1 import Model1
from cgmes242.operation import Operation
from cgmes242.package_name import PackageName
from cgmes242.primitive import Primitive
from cgmes242.profile_1 import Profile1
from cgmes242.rb import Rb
from cgmes242.rt import Rt
from cgmes242.seqno import Seqno
from cgmes242.short_circuit import ShortCircuit
from cgmes242.sourcestyle import Sourcestyle
from cgmes242.style_3 import Style3
from cgmes242.tagged import Tagged
from cgmes242.tpos import Tpos
from cgmes242.virtual_inheritance import VirtualInheritance

__NAMESPACE__ = "http://schema.omg.org/spec/XMI/2.1"


@dataclass
class Xmi:
    class Meta:
        name = "XMI"
        namespace = "http://schema.omg.org/spec/XMI/2.1"

    version: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schema.omg.org/spec/XMI/2.1",
            "required": True,
        },
    )
    documentation: Optional[Documentation1] = field(
        default=None,
        metadata={
            "name": "Documentation",
            "type": "Element",
            "required": True,
        },
    )
    model: Optional[Model1] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/UML/20090901",
            "required": True,
        },
    )
    extension: Optional[Extension] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "required": True,
        },
    )
    entsoe: list[Entsoe] = field(
        default_factory=list,
        metadata={
            "name": "Entsoe",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    enumeration: list[Enumeration] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/EAUML/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    enum: list[EnumType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    guidbased_on: list[GuidbasedOn] = field(
        default_factory=list,
        metadata={
            "name": "GUIDBasedOn",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    cimdatatype: list[Cimdatatype] = field(
        default_factory=list,
        metadata={
            "name": "CIMDatatype",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    is_based_on: list[IsBasedOn] = field(
        default_factory=list,
        metadata={
            "name": "IsBasedOn",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    primitive: list[Primitive] = field(
        default_factory=list,
        metadata={
            "name": "Primitive",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    compound: list[Compound] = field(
        default_factory=list,
        metadata={
            "name": "Compound",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    operation: list[Operation] = field(
        default_factory=list,
        metadata={
            "name": "Operation",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/BPMN2.0/1.5",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    short_circuit: list[ShortCircuit] = field(
        default_factory=list,
        metadata={
            "name": "ShortCircuit",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    profile: list[Profile1] = field(
        default_factory=list,
        metadata={
            "name": "Profile",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    cim_is_rdf_about: list[CimIsRdfAbout] = field(
        default_factory=list,
        metadata={
            "name": "CIM_IsRdfAbout",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    description: list[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    sourcestyle: list[Sourcestyle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    callout: list[Callout] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/Whiteboard/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    virtual_inheritance: list[VirtualInheritance] = field(
        default_factory=list,
        metadata={
            "name": "virtualInheritance",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    style: list[Style3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    rb: list[Rb] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    linemode: list[Linemode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ea_src_xref_property: list[EaSrcXrefProperty] = field(
        default_factory=list,
        metadata={
            "name": "__ea_src_xref_property",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ea_dst_xref_property: list[EaDstXrefProperty] = field(
        default_factory=list,
        metadata={
            "name": "__ea_dst_xref_property",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    rt: list[Rt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    seqno: list[Seqno] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    head_style: list[HeadStyle] = field(
        default_factory=list,
        metadata={
            "name": "headStyle",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    lb: list[Lb] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    ea_type: list[EaType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    line_style: list[LineStyle] = field(
        default_factory=list,
        metadata={
            "name": "lineStyle",
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    lt: list[Lt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    deststyle: list[Deststyle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    package_name: list[PackageName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    tagged: list[Tagged] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    tpos: list[Tpos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    date_modified: list[DateModified] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    date_created: list[DateCreated] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/thecustomprofile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sparxsystems.com/profiles/EPProfile/1.0",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
