from __future__ import annotations
from ...DomainProfile.Capacitance import Capacitance
from ...DomainProfile.Resistance import Resistance
from ...DomainProfile.Voltage import Voltage
from .DCConductingEquipment import DCConductingEquipment
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class DCShunt(DCConductingEquipment):
    capacitance: Capacitance = field(metadata={'xpath': 'cim:DCShunt.capacitance'})
    ratedUdc: Voltage = field(metadata={'xpath': 'cim:DCShunt.ratedUdc'})
    resistance: Resistance = field(metadata={'xpath': 'cim:DCShunt.resistance'})
