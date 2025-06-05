from __future__ import annotations
from ..Core.ACDCTerminal import ACDCTerminal
from ..Core.Equipment import Equipment
from ..Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class OperationalLimitSet(IdentifiedObject):
    Equipment_id: str | None = field(default=None, metadata={"xpath": "cim:OperationalLimitSet.Equipment/@rdf:resource", "pattern": r"^#.+$"})
    Equipment_ref: Equipment | None = None
    Terminal_id: str | None = field(default=None, metadata={"xpath": "cim:OperationalLimitSet.Terminal/@rdf:resource", "pattern": r"^#.+$"})
    Terminal_ref: ACDCTerminal | None = None
