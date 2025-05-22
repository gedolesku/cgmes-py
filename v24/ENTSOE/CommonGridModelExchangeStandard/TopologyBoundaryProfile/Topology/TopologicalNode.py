from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.String import String     
from ENTSOE.CommonGridModelExchangeStandard.TopologyBoundaryProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.TopologyBoundaryProfile.Core.ConnectivityNodeContainer import ConnectivityNodeContainer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.TopologyBoundaryProfile.Core.ConnectivityNode import ConnectivityNode     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.TopologyBoundaryProfile.Core.BaseVoltage import BaseVoltage     

@dataclass
class TopologicalNode(IdentifiedObject):
    """For a detailed substation model a topological node is a set of connectivity
    nodes that, in the current network state, are connected together through any
    type of closed switches, including  jumpers. Topological nodes change as the
    current network state changes (i.e., switches, breakers, etc. change state).
      For a planning model, switch statuses are not used to form topological nodes.
    Instead they are manually created or deleted in a model builder tool.
    Topological nodes maintained this way are also called "busses".
    """
    # Identifies if a node is a BoundaryPoint. If boundaryPoint=true the
    # ConnectivityNode or the TopologicalNode represents a BoundaryPoint. 
    boundaryPoint: bool  = None
 
    # The attribute is used for an exchange of the ISO code of the region to which
    # the “From” side of the Boundary point belongs to or it is connected to.
    # The ISO code is two characters country code as defined by ISO 3166 (<a
    # href="{???????????')"><font color="#0000ff"><u>http://www.iso.
    # org/iso/country_codes</u></font></a>). The length of the string is 2 characters
    # maximum.
    # The attribute is a required for the Boundary Model Authority Set where this
    # attribute is used only for the TopologicalNode in the Boundary Topology profile
    # and ConnectivityNode in the Boundary Equipment profile.
    fromEndIsoCode: str  = None
 
    # The attribute is used for an exchange of a human readable name with length of
    # the string 32 characters maximum. The attribute covers two cases:
    # <ul>
    # 	<li>if the Boundary point is <b>placed on a tie-line</b> the attribute is used
    # for exchange of the geographical name of the <b>substation</b> to which the
    # “From” side of the tie-line is connected to.</li>
    # 	<li>if the Boundary point is <b>placed in a substation</b> the attribute is
    # used for exchange of the name of the <b>element</b> (e.g. PowerTransformer,
    # ACLineSegment, Switch, etc) to which the “From” side of the Boundary point is
    # connected to.</li>
    # </ul>
    # The attribute is required for the Boundary Model Authority Set where it is used
    # only for the TopologicalNode in the Boundary Topology profile and
    # ConnectivityNode in the Boundary Equipment profile.
    fromEndName: str  = None
 
    # The attribute is used for an exchange of the name of the TSO to which the
    # “From” side of the Boundary point belongs to or it is connected to. The length
    # of the string is 32 characters maximum.
    # The attribute is required for the Boundary Model Authority Set where it is used
    # only for the TopologicalNode in the Boundary Topology profile and
    # ConnectivityNode in the Boundary Equipment profile. 
    fromEndNameTso: str  = None
 
    # The attribute is used for an exchange of the ISO code of the region to which
    # the “To” side of the Boundary point belongs to or it is connected to.
    # The ISO code is two characters country code as defined by ISO 3166 (<a
    # href="{???????????')"><font color="#0000ff"><u>http://www.iso.
    # org/iso/country_codes</u></font></a>). The length of the string is 2 characters
    # maximum.
    # The attribute is a required for the Boundary Model Authority Set where this
    # attribute is used only for the TopologicalNode in the Boundary Topology profile
    # and ConnectivityNode in the Boundary Equipment profile.
    toEndIsoCode: str  = None
 
    # The attribute is used for an exchange of a human readable name with length of
    # the string 32 characters maximum. The attribute covers two cases:
    # <ul>
    # 	<li>if the Boundary point is <b>placed on a tie-line</b> the attribute is used
    # for exchange of the geographical name of the <b>substation</b> to which the
    # “To” side of the tie-line is connected to.</li>
    # 	<li>if the Boundary point is <b>placed in a substation</b> the attribute is
    # used for exchange of the name of the <b>element</b> (e.g. PowerTransformer,
    # ACLineSegment, Switch, etc) to which the “To” side of the Boundary point is
    # connected to.</li>
    # </ul>
    # The attribute is required for the Boundary Model Authority Set where it is used
    # only for the TopologicalNode in the Boundary Topology profile and
    # ConnectivityNode in the Boundary Equipment profile.
    toEndName: str  = None
 
    # The attribute is used for an exchange of the name of the TSO to which the “To”
    # side of the Boundary point belongs to or it is connected to. The length of the
    # string is 32 characters maximum.
    # The attribute is required for the Boundary Model Authority Set where it is used
    # only for the TopologicalNode in the Boundary Topology profile and
    # ConnectivityNode in the Boundary Equipment profile. 
    toEndNameTso: str  = None
 
    # The connectivity node container to which the toplogical node belongs.
    ConnectivityNodeContainer_ref: Optional[ConnectivityNodeContainer] = None
    ConnectivityNodeContainer: str = None
 
    # The connectivity nodes combine together to form this topological node.  May
    # depend on the current state of switches in the network.
    ConnectivityNodes: List[ConnectivityNode]  = field(default_factory=list)
 
    # The base voltage of the topologocial node.
    BaseVoltage_ref: Optional[BaseVoltage] = None
    BaseVoltage: str = None
     