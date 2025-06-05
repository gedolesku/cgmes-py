from __future__ import annotations
from .TapChanger import TapChanger
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class RatioTapChanger(TapChanger):
    pass
