from __future__ import annotations
from ...DomainProfile.UnitSymbol import UnitSymbol
from .CurveStyle import CurveStyle
from .IdentifiedObject import IdentifiedObject
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class Curve(Protocol):
    curveStyle: CurveStyle  # metadata: cim='cim:Curve.curveStyle', mult='1'
    xUnit: UnitSymbol  # metadata: cim='cim:Curve.xUnit', mult='1'
    y1Unit: UnitSymbol  # metadata: cim='cim:Curve.y1Unit', mult='1'
    y2Unit: Optional[UnitSymbol]  # metadata: cim='cim:Curve.y2Unit', mult='0..1'
