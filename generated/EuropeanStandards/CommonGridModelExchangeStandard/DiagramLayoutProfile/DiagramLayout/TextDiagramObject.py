from __future__ import annotations
from ...DomainProfile.String import String
from .DiagramObject import DiagramObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class TextDiagramObject(DiagramObject):
    text: String = field(metadata={'xpath': 'cim:TextDiagramObject.text'})
