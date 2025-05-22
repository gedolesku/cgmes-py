from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.CurveStyle import CurveStyle     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitSymbol import UnitSymbol     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.CurveData import CurveData     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class Curve(IdentifiedObject):
    """A multi-purpose curve or functional relationship between an independent
    variable (X-axis) and dependent (Y-axis) variables.
    """
    # The style or shape of the curve.
    curveStyle_: CurveStyle  = None
 
    # The X-axis units of measure.
    xUnit_: UnitSymbol  = None
 
    # The Y1-axis units of measure.
    y1Unit_: UnitSymbol  = None
 
    # The Y2-axis units of measure.
    y2Unit_: UnitSymbol  = None
 
    # The curve of  this curve data point.
    CurveData_: List[CurveData]  = field(default_factory=list)
     