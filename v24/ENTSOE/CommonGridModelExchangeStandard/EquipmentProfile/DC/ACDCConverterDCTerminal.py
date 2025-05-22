from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCPolarityKind import DCPolarityKind     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCBaseTerminal import DCBaseTerminal
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.ACDCConverter import ACDCConverter     

@dataclass
class ACDCConverterDCTerminal(DCBaseTerminal):
    """A DC electrical connection point at the AC/DC converter. The AC/DC converter is
    electrically connected also to the AC side. The AC connection is inherited from
    the AC conducting equipment in the same way as any other AC equipment. The
    AC/DC converter DC terminal is separate from generic DC terminal to restrict
    the connection with the AC side to AC/DC converter and so that no other DC
    conducting equipment can be connected to the AC side.
    """
    # Represents the normal network polarity condition.
    polarity_: DCPolarityKind  = None
 
    ACDCConverter_: Optional[ACDCConverter] = None
     