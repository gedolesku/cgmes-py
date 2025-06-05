from __future__ import annotations
from .AnalogControl import AnalogControl
from .ValueAliasSet import ValueAliasSet
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class RaiseLowerCommand(AnalogControl):
    ValueAliasSet_id: str | None = field(default=None, metadata={"xpath": "cim:RaiseLowerCommand.ValueAliasSet/@rdf:resource", "pattern": r"^#.+$"})
    ValueAliasSet_ref: ValueAliasSet | None = None
