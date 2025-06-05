from __future__ import annotations
from ...DomainProfile.Inductance import Inductance
from ...DomainProfile.Resistance import Resistance
from ...DomainProfile.Voltage import Voltage
from .DCConductingEquipment import DCConductingEquipment
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class DCSeriesDevice(DCConductingEquipment):
    inductance: Inductance = field(metadata={'xpath': 'cim:DCSeriesDevice.inductance'})
    ratedUdc: Voltage = field(metadata={'xpath': 'cim:DCSeriesDevice.ratedUdc'})
    resistance: Resistance = field(metadata={'xpath': 'cim:DCSeriesDevice.resistance'})
