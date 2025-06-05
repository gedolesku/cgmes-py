from __future__ import annotations
from ...DomainProfile.AngleDegrees import AngleDegrees
from ...DomainProfile.Voltage import Voltage
from .ACDCConverter import ACDCConverter
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class VsConverter(ACDCConverter):
    delta: AngleDegrees = field(metadata={'xpath': 'cim:VsConverter.delta'})
    uf: Voltage = field(metadata={'xpath': 'cim:VsConverter.uf'})
