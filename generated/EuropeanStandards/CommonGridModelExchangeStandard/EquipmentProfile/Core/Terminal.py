from __future__ import annotations
from .ACDCTerminal import ACDCTerminal
from .ConductingEquipment import ConductingEquipment
from .ConnectivityNode import ConnectivityNode
from .PhaseCode import PhaseCode
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class Terminal(ACDCTerminal):
    ConductingEquipment_id: str | None = field(default=None, metadata={"xpath": "cim:Terminal.ConductingEquipment/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    ConductingEquipment_ref: ConductingEquipment = None
    ConnectivityNode_id: str | None = field(default=None, metadata={"xpath": "cim:Terminal.ConnectivityNode/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    ConnectivityNode_ref: ConnectivityNode = None
    phases: Optional[PhaseCode] = field(default=None, metadata={'xpath': 'cim:Terminal.phases'})
