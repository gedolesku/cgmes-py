from __future__ import annotations
from ...DomainProfile.Integer import Integer
from ..Core.IdentifiedObject import IdentifiedObject
from ..Core.ReportingGroup import ReportingGroup
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class BusNameMarker(IdentifiedObject):
    priority: Optional[Integer] = field(default=None, metadata={'xpath': 'cim:BusNameMarker.priority'})
    ReportingGroup_id: str | None = field(default=None, metadata={"xpath": "cim:BusNameMarker.ReportingGroup/@rdf:resource", "pattern": r"^#.+$"})
    ReportingGroup_ref: ReportingGroup | None = None
