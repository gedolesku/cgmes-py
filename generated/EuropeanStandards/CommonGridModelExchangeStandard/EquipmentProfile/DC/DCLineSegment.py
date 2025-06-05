from __future__ import annotations
from ...DomainProfile.Capacitance import Capacitance
from ...DomainProfile.Inductance import Inductance
from ...DomainProfile.Length import Length
from ...DomainProfile.Resistance import Resistance
from .DCConductingEquipment import DCConductingEquipment
from .PerLengthDCLineParameter import PerLengthDCLineParameter
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class DCLineSegment(DCConductingEquipment):
    capacitance: Optional[Capacitance] = field(default=None, metadata={'xpath': 'cim:DCLineSegment.capacitance'})
    inductance: Optional[Inductance] = field(default=None, metadata={'xpath': 'cim:DCLineSegment.inductance'})
    length: Optional[Length] = field(default=None, metadata={'xpath': 'cim:DCLineSegment.length'})
    resistance: Optional[Resistance] = field(default=None, metadata={'xpath': 'cim:DCLineSegment.resistance'})
    PerLengthParameter_id: str | None = field(default=None, metadata={"xpath": "cim:DCLineSegment.PerLengthParameter/@rdf:resource", "pattern": r"^#.+$"})
    PerLengthParameter_ref: PerLengthDCLineParameter | None = None
