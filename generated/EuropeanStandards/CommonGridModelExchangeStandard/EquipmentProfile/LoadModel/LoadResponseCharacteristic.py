from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.Simple_Float import Simple_Float
from ..Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class LoadResponseCharacteristic(IdentifiedObject):
    exponentModel: Boolean = field(metadata={'xpath': 'cim:LoadResponseCharacteristic.exponentModel'})
    pConstantCurrent: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadResponseCharacteristic.pConstantCurrent'})
    pConstantImpedance: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadResponseCharacteristic.pConstantImpedance'})
    pConstantPower: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadResponseCharacteristic.pConstantPower'})
    pFrequencyExponent: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadResponseCharacteristic.pFrequencyExponent'})
    pVoltageExponent: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadResponseCharacteristic.pVoltageExponent'})
    qConstantCurrent: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadResponseCharacteristic.qConstantCurrent'})
    qConstantImpedance: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadResponseCharacteristic.qConstantImpedance'})
    qConstantPower: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadResponseCharacteristic.qConstantPower'})
    qFrequencyExponent: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadResponseCharacteristic.qFrequencyExponent'})
    qVoltageExponent: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:LoadResponseCharacteristic.qVoltageExponent'})
