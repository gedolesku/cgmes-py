from __future__ import annotations
from ..Wires.EnergyConsumer import EnergyConsumer
from .NonConformLoadGroup import NonConformLoadGroup
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class NonConformLoad(EnergyConsumer):
    LoadGroup_id: str | None = field(default=None, metadata={"xpath": "cim:NonConformLoad.LoadGroup/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    LoadGroup_ref: NonConformLoadGroup = None
