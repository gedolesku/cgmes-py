from __future__ import annotations
from ...DomainProfile.Voltage import Voltage
from .IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class BaseVoltage(IdentifiedObject):
    nominalVoltage: Voltage = field(metadata={'xpath': 'cim:BaseVoltage.nominalVoltage'})
