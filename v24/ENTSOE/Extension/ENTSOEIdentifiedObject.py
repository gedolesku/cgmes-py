from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.String import String     

@dataclass
class ENTSOEIdentifiedObject:
    """This is a class extension of the class IdentifiedObject in CIM. The extension
    is done for the purpose of ENTSO-E profiling work.
    """
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
    energyIdentCodeEic_: str  = None
 
    # The attribute is used for an exchange of a human readable short name with
    # length of the string 12 characters maximum.
    shortName_: str  = None
     