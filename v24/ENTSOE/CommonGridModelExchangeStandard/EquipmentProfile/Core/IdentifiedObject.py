from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.String import String     

@dataclass
class IdentifiedObject:
    """This is a root class to provide common identification for all classes needing
    identification and naming attributes.
    """
    # The description is a free human readable text describing or naming the object.
    # It may be non unique and may not correlate to a naming hierarchy.
    description: str  = None
 
    # The attribute is used for an exchange of the EIC code (Energy identification
    # Code). The length of the string is 16 characters as defined by the EIC code.
    # References:
    # <ul>
    # 	<li>Local issuing offices for EIC: <a
    # href="{???????????????????????????}???')"><font color="#0000ff"><u>https://www.
    # entsoe.eu/publications/edi-library/links-to-eic-websites/</u></font></a> </li>
    # 	<li>EIC description: <a href="{????????????????? ')"><font
    # color="#0000ff"><u>https://www.entsoe.eu/index.
    # php?id=73&libCat=eic</u></font></a> .</li>
    # </ul>
    energyIdentCodeEic: str  = None
 
    # Master resource identifier issued by a model authority. The mRID is globally
    # unique within an exchange context. Global uniqueness is easily achieved by
    # using a UUID,  as specified in RFC 4122, for the mRID.  The use of UUID is
    # strongly recommended.
    # For CIMXML data files in RDF syntax conforming to IEC 61970-552 Edition 1, the
    # mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object
    # elements.
    mRID: str  = None
 
    # The name is any free human readable and possibly non unique text naming the
    # object.
    name: str  = None
 
    # The attribute is used for an exchange of a human readable short name with
    # length of the string 12 characters maximum.
    shortName: str  = None
     