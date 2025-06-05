from __future__ import annotations
from .ACDCConverter import ACDCConverter
from .DCBaseTerminal import DCBaseTerminal
from .DCPolarityKind import DCPolarityKind
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class ACDCConverterDCTerminal(DCBaseTerminal):
    DCConductingEquipment_id: str | None = field(default=None, metadata={"xpath": "cim:ACDCConverterDCTerminal.DCConductingEquipment/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    DCConductingEquipment_ref: ACDCConverter = None
    polarity: Optional[DCPolarityKind] = field(default=None, metadata={'xpath': 'cim:ACDCConverterDCTerminal.polarity'})
