from __future__ import annotations
from .PhaseTapChanger import PhaseTapChanger
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PhaseTapChangerLinear(PhaseTapChanger):
    pass
