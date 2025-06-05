from __future__ import annotations
from ...DomainProfile.AngleDegrees import AngleDegrees
from .ACDCConverter import ACDCConverter
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class CsConverter(ACDCConverter):
    alpha: AngleDegrees = field(metadata={'xpath': 'cim:CsConverter.alpha'})
    gamma: AngleDegrees = field(metadata={'xpath': 'cim:CsConverter.gamma'})
