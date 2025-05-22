from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.CurrentFlow import CurrentFlow     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.ACDCConverter import ACDCConverter
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.VsCapabilityCurve import VsCapabilityCurve     

@dataclass
class VsConverter(ACDCConverter):
    """DC side of the voltage source converter (VSC).
    """
    # The max quotient between the AC converter voltage (Uc) and DC voltage (Ud). A
    # factor typically less than 1. VSC configuration data used in power flow.
    maxModulationIndex_: Simple_Float  = None
 
    # The maximum current through a valve. This current limit is the basis for
    # calculating the capability diagram. VSC  configuration data.
    maxValveCurrent_: CurrentFlow  = None
 
    # All converters with this capability curve.
    VsCapabilityCurve_: Optional[VsCapabilityCurve] = None
     