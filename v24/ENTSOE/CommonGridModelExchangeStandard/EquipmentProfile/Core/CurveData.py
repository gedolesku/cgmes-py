from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Curve import Curve     

@dataclass
class CurveData:
    """Multi-purpose data points for defining a curve.  The use of this generic class
    is discouraged if a more specific class  can be used to specify the x and y
    axis values along with their specific data types.
    """
    # The data value of the X-axis variable,  depending on the X-axis units.
    xvalue_: Simple_Float  = None
 
    # The data value of the  first Y-axis variable, depending on the Y-axis units.
    y1value_: Simple_Float  = None
 
    # The data value of the second Y-axis variable (if present), depending on the Y-
    # axis units.
    y2value_: Simple_Float  = None
 
    # The point data values that define this curve.
    Curve_: Optional[Curve] = None
     