from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.String import String     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Date import Date     

@dataclass
class TopologyVersion:
    """Version details.
    """
    # Base UML provided by CIM model manager.
    baseUML_: str  = "iec61970cim16v28_iec61968cim12v08_iec62325cim03v01a"
 
    # Profile URI used in the Model Exchange header and defined in IEC standards.  It
    # uniquely identifies the Profile and its version. It is given for information
    # only and to identify the closest IEC profile to which this CGMES profile is
    # based on.
    baseURI_: str  = "http://iec.ch/TC57/2013/61970-456/Topology/4"
 
    # Profile creation date
    # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.
    date_: str  ="2014-06-23"
 
    # Difference model URI defined by IEC 61970-552. 
    differenceModelURI_: str  = "http://iec.ch/TC57/61970-552/DifferenceModel/1#"
 
    # UML provided by ENTSO-E.
    entsoeUML_: str  = "entsoe_v2.4.15"
 
    # Profile URI defined by ENTSO-E and used in the Model Exchange header.  It
    # uniquely identifies the Profile and its version. The last two elements in the
    # URI (http://entsoe.eu/CIM/Topology/yy/zzz) indicate major and minor versions
    # where:
    # - yy - indicates a major version;
    # - zzz - indicates a minor version. 
    entsoeURI_: str  = "http://entsoe.eu/CIM/Topology/4/1"
 
    # Model Description URI defined by IEC 61970-552. 
    modelDescriptionURI_: str  = "http://iec.ch/TC57/61970-552/ModelDescription/1#"
 
    # RDF namespace. 
    namespaceRDF_: str  = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
 
    # CIM UML namespace. 
    namespaceUML_: str  = "http://iec.ch/TC57/2013/CIM-schema-cim16#"
 
    # The short name of the profile used in profile documentation.
    shortName_: str  = "TP"
     