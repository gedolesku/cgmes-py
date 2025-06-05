from __future__ import annotations
from ..Wires.EnergyConsumer import EnergyConsumer
from .ConformLoadGroup import ConformLoadGroup
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ConformLoad(EnergyConsumer):
    LoadGroup_id: str | None = field(default=None, metadata={"xpath": "cim:ConformLoad.LoadGroup/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    LoadGroup_ref: ConformLoadGroup = None
