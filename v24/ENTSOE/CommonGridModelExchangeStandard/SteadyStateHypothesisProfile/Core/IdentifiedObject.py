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
    # Master resource identifier issued by a model authority. The mRID is globally
    # unique within an exchange context. Global uniqueness is easily achieved by
    # using a UUID,  as specified in RFC 4122, for the mRID.  The use of UUID is
    # strongly recommended.
    # For CIMXML data files in RDF syntax conforming to IEC 61970-552 Edition 1, the
    # mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object
    # elements.
    mRID_: str  = None
 
    # The name is any free human readable and possibly non unique text naming the
    # object.
    name_: str  = None
     