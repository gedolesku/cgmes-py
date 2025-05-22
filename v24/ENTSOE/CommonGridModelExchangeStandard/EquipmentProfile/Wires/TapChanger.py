from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.TapChangerControl import TapChangerControl     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.PowerSystemResource import PowerSystemResource

@dataclass
class TapChanger(PowerSystemResource):
    """Mechanism for changing transformer winding tap positions.
    """
    # Highest possible tap step position, advance from neutral.
    # The attribute shall be greater than lowStep.
    highStep: int  = None
 
    # Lowest possible tap step position, retard from neutral
    lowStep: int  = None
 
    # Specifies whether or not a TapChanger has load tap changing capabilities.
    ltcFlag: bool  = None
 
    # The neutral tap step position for this winding.
    # The attribute shall be equal or greater than lowStep and equal or less than
    # highStep.
    neutralStep: int  = None
 
    # Voltage at which the winding operates at the neutral tap setting.
    neutralU: Voltage  = None
 
    # The tap step position used in "normal" network operation for this winding. For
    # a "Fixed" tap changer indicates the current physical tap setting.
    # The attribute shall be equal or greater than lowStep and equal or less than
    # highStep.
    normalStep: int  = None
 
    # The tap changers that participates in this regulating tap control scheme.
    TapChangerControl_ref: Optional[TapChangerControl] = None
    TapChangerControl: str = None
     