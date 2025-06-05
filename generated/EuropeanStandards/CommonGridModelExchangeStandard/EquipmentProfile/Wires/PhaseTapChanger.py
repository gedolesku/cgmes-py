from __future__ import annotations
from .TapChanger import TapChanger
from .TransformerEnd import TransformerEnd
from typing import Protocol, runtime_checkable

@runtime_checkable
class PhaseTapChanger(TapChanger, Protocol):
    TransformerEnd_ref: TransformerEnd  # metadata: cim='cim:PhaseTapChanger.TransformerEnd', mult='1'
    TransformerEnd_id: str
