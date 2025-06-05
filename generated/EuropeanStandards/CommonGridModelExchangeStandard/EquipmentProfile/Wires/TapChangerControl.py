from __future__ import annotations
from .RegulatingControl import RegulatingControl
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class TapChangerControl(RegulatingControl):
    pass
