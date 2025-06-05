from __future__ import annotations
from ...DomainProfile.Simple_Float import Simple_Float
from ..Wires.TapChanger import TapChanger
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class SvTapStep:
    position: Simple_Float = field(metadata={'xpath': 'cim:SvTapStep.position'})
    TapChanger_id: str | None = field(default=None, metadata={"xpath": "cim:SvTapStep.TapChanger/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    TapChanger_ref: TapChanger = None
