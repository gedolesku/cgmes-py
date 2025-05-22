from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCConverterOperatingModeKind import DCConverterOperatingModeKind     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.DC.DCEquipmentContainer import DCEquipmentContainer

@dataclass
class DCConverterUnit(DCEquipmentContainer):
    """Indivisible operative unit comprising all equipment between the point of common
    coupling on the AC side and the point of common coupling – DC side, essentially
    one or more converters, together with one or more converter transformers,
    converter control equipment, essential protective and switching devices and
    auxiliaries, if any, used for conversion.
    """
    operationMode_: DCConverterOperatingModeKind  = None
     