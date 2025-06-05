from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.CurrentFlow import CurrentFlow
from ...DomainProfile.Reactance import Reactance
from ...DomainProfile.Resistance import Resistance
from ...DomainProfile.Voltage import Voltage
from ..Core.ConductingEquipment import ConductingEquipment
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class SeriesCompensator(ConductingEquipment):
    r: Resistance = field(metadata={'xpath': 'cim:SeriesCompensator.r'})
    r0: Resistance = field(metadata={'xpath': 'cim:SeriesCompensator.r0'})
    varistorPresent: Boolean = field(metadata={'xpath': 'cim:SeriesCompensator.varistorPresent'})
    varistorRatedCurrent: CurrentFlow = field(metadata={'xpath': 'cim:SeriesCompensator.varistorRatedCurrent'})
    varistorVoltageThreshold: Voltage = field(metadata={'xpath': 'cim:SeriesCompensator.varistorVoltageThreshold'})
    x: Reactance = field(metadata={'xpath': 'cim:SeriesCompensator.x'})
    x0: Reactance = field(metadata={'xpath': 'cim:SeriesCompensator.x0'})
