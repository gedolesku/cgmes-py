from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.String import String     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Date import Date     

@dataclass
class DomainVersion:
    """Version details.
    """
    # Base UML provided by CIM model manager.
    baseUML: str  = "iec61970cim16v28_iec61968cim12v08_iec62325cim03v01a"
 
    # Profile creation date
    # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.
    date: str  ="2014-05-28"
 
    # UML provided by ENTSO-E.
    entsoeUML: str  = "entsoe_v2.4.14"
 
    # Domain version define in the following format: yy.zzz where:
    # - yy - indicates a major version;
    # - zzz - indicates a minor version.
    version: str  = "2.4.14"
     