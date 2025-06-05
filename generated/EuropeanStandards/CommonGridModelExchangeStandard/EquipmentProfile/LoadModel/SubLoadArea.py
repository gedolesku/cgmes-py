from __future__ import annotations
from .EnergyArea import EnergyArea
from .LoadArea import LoadArea
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class SubLoadArea(EnergyArea):
    LoadArea_id: str | None = field(default=None, metadata={"xpath": "cim:SubLoadArea.LoadArea/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    LoadArea_ref: LoadArea = None
