from __future__ import annotations
from ...DomainProfile.AngleRadians import AngleRadians
from ...DomainProfile.Reactance import Reactance
from ...DomainProfile.Resistance import Resistance
from ...DomainProfile.Voltage import Voltage
from ..Core.ConductingEquipment import ConductingEquipment
from .EnergySchedulingType import EnergySchedulingType
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class EnergySource(ConductingEquipment):
    nominalVoltage: Optional[Voltage] = field(default=None, metadata={'xpath': 'cim:EnergySource.nominalVoltage'})
    r: Optional[Resistance] = field(default=None, metadata={'xpath': 'cim:EnergySource.r'})
    r0: Optional[Resistance] = field(default=None, metadata={'xpath': 'cim:EnergySource.r0'})
    rn: Optional[Resistance] = field(default=None, metadata={'xpath': 'cim:EnergySource.rn'})
    voltageAngle: Optional[AngleRadians] = field(default=None, metadata={'xpath': 'cim:EnergySource.voltageAngle'})
    voltageMagnitude: Optional[Voltage] = field(default=None, metadata={'xpath': 'cim:EnergySource.voltageMagnitude'})
    x: Optional[Reactance] = field(default=None, metadata={'xpath': 'cim:EnergySource.x'})
    x0: Optional[Reactance] = field(default=None, metadata={'xpath': 'cim:EnergySource.x0'})
    xn: Optional[Reactance] = field(default=None, metadata={'xpath': 'cim:EnergySource.xn'})
    EnergySchedulingType_id: str | None = field(default=None, metadata={"xpath": "cim:EnergySource.EnergySchedulingType/@rdf:resource", "pattern": r"^#.+$"})
    EnergySchedulingType_ref: EnergySchedulingType | None = None
