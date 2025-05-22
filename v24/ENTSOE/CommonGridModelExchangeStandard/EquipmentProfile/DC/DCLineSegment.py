from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Capacitance import Capacitance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Inductance import Inductance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Length import Length     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.PerLengthDCLineParameter import PerLengthDCLineParameter     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCConductingEquipment import DCConductingEquipment

@dataclass
class DCLineSegment(DCConductingEquipment):
    """A wire or combination of wires not insulated from one another, with consistent
    electrical characteristics, used to carry direct current between points in the
    DC region of the power system.
    """
    # Capacitance of the DC line segment. Significant for cables only.
    capacitance: Capacitance  = None
 
    # Inductance of the DC line segment. Neglectable compared with DCSeriesDevice
    # used for smoothing.
    inductance: Inductance  = None
 
    # Resistance of the DC line segment.
    resistance: Resistance  = None
 
    # Segment length for calculating line section capabilities.
    length: Length  = None
 
    # Set of per-length parameters for this line segment.
    PerLengthParameter_ref: Optional[PerLengthDCLineParameter] = None
    PerLengthParameter: str = None
     