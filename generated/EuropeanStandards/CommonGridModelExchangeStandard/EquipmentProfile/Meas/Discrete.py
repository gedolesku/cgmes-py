from __future__ import annotations
from .Measurement import Measurement
from .ValueAliasSet import ValueAliasSet
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class Discrete(Measurement):
    ValueAliasSet_id: str | None = field(default=None, metadata={"xpath": "cim:Discrete.ValueAliasSet/@rdf:resource", "pattern": r"^#.+$"})
    ValueAliasSet_ref: ValueAliasSet | None = None
