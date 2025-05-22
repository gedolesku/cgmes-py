from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.CapacitancePerLength import CapacitancePerLength     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.InductancePerLength import InductancePerLength     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ResistancePerLength import ResistancePerLength     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCLineSegment import DCLineSegment     

@dataclass
class PerLengthDCLineParameter:
    # Capacitance per unit of length of the DC line segment; significant for cables
    # only.
    capacitance_: CapacitancePerLength  = None
 
    # Inductance per unit of length of the DC line segment.
    inductance_: InductancePerLength  = None
 
    # Resistance per length of the DC line segment.
    resistance_: ResistancePerLength  = None
 
    # All line segments described by this set of per-length parameters.
    DCLineSegment_: List[DCLineSegment]  = field(default_factory=list)
     