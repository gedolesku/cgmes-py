from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.ControlArea.ControlAreaTypeKind import ControlAreaTypeKind     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.PowerSystemResource import PowerSystemResource
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.EnergyArea import EnergyArea     

@dataclass
class ControlArea(PowerSystemResource):
    """A control area<b> </b>is a grouping of generating units and/or loads and a
    cutset of tie lines (as terminals) which may be used for a variety of purposes
    including automatic generation control, powerflow solution area interchange
    control specification, and input to load forecasting.   Note that any number of
    overlapping control area specifications can be superimposed on the physical
    model.
    """
    # The primary type of control area definition used to determine if this is used
    # for automatic generation control, for planning interchange control, or other
    # purposes.   A control area specified with primary type of automatic generation
    # control could still be forecast and used as an interchange area in power flow
    # analysis.
    type_: ControlAreaTypeKind  = None
 
    # The energy area that is forecast from this control area specification.
    EnergyArea_: Optional[EnergyArea] = None
     