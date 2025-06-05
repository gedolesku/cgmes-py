from __future__ import annotations
from ...DomainProfile.Integer import Integer
from ..Core.IdentifiedObject import IdentifiedObject
from .ValueAliasSet import ValueAliasSet
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class ValueToAlias(IdentifiedObject):
    value: Integer = field(metadata={'xpath': 'cim:ValueToAlias.value'})
    ValueAliasSet_id: str | None = field(default=None, metadata={"xpath": "cim:ValueToAlias.ValueAliasSet/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    ValueAliasSet_ref: ValueAliasSet = None
