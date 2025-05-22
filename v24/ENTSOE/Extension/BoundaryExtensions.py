from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.String import String     

@dataclass
class BoundaryExtensions:
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
     