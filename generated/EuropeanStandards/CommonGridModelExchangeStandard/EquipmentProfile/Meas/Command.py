from __future__ import annotations
from ...DomainProfile.Integer import Integer
from .Control import Control
from .DiscreteValue import DiscreteValue
from .ValueAliasSet import ValueAliasSet
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class Command(Control):
    normalValue: Integer = field(metadata={'xpath': 'cim:Command.normalValue'})
    value: Integer = field(metadata={'xpath': 'cim:Command.value'})
    DiscreteValue_id: str | None = field(default=None, metadata={"xpath": "cim:Command.DiscreteValue/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    DiscreteValue_ref: DiscreteValue = None
    ValueAliasSet_id: str | None = field(default=None, metadata={"xpath": "cim:Command.ValueAliasSet/@rdf:resource", "pattern": r"^#.+$"})
    ValueAliasSet_ref: ValueAliasSet | None = None
