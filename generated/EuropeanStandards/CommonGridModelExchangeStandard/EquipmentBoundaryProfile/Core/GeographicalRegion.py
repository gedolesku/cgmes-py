from __future__ import annotations
from .IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GeographicalRegion(IdentifiedObject):
    pass
