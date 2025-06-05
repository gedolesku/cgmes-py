from __future__ import annotations
from ...DomainProfile.CapacitancePerLength import CapacitancePerLength
from ...DomainProfile.InductancePerLength import InductancePerLength
from ...DomainProfile.ResistancePerLength import ResistancePerLength
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class PerLengthDCLineParameter:
    capacitance: Optional[CapacitancePerLength] = field(default=None, metadata={'xpath': 'cim:PerLengthDCLineParameter.capacitance'})
    inductance: Optional[InductancePerLength] = field(default=None, metadata={'xpath': 'cim:PerLengthDCLineParameter.inductance'})
    resistance: Optional[ResistancePerLength] = field(default=None, metadata={'xpath': 'cim:PerLengthDCLineParameter.resistance'})
