from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PerCent import PerCent     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ReactivePower import ReactivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.LoadModel.LoadResponseCharacteristic import LoadResponseCharacteristic     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class EnergyConsumer(ConductingEquipment):
    """Generic user of energy - a  point of consumption on the power system model.
    """
    # Active power of the load that is a fixed quantity. Load sign convention is used,
    # i.e. positive sign means flow out from a node.
    pfixed_: ActivePower  = None
 
    # Fixed active power as per cent of load group fixed active power. Load sign
    # convention is used, i.e. positive sign means flow out from a node.
    pfixedPct_: PerCent  = None
 
    # Reactive power of the load that is a fixed quantity. Load sign convention is
    # used, i.e. positive sign means flow out from a node.
    qfixed_: ReactivePower  = None
 
    # Fixed reactive power as per cent of load group fixed reactive power. Load sign
    # convention is used, i.e. positive sign means flow out from a node.
    qfixedPct_: PerCent  = None
 
    # The load response characteristic of this load.  If missing, this load is
    # assumed to be constant power.
    LoadResponseCharacteristic_: Optional[LoadResponseCharacteristic] = None
     