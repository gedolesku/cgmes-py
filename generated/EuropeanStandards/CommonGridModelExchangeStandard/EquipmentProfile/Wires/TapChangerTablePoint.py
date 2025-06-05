from __future__ import annotations
from ...DomainProfile.Integer import Integer
from ...DomainProfile.PerCent import PerCent
from ...DomainProfile.Simple_Float import Simple_Float
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class TapChangerTablePoint:
    step: Integer = field(metadata={'xpath': 'cim:TapChangerTablePoint.step'})
    b: Optional[PerCent] = field(default=None, metadata={'xpath': 'cim:TapChangerTablePoint.b'})
    g: Optional[PerCent] = field(default=None, metadata={'xpath': 'cim:TapChangerTablePoint.g'})
    r: Optional[PerCent] = field(default=None, metadata={'xpath': 'cim:TapChangerTablePoint.r'})
    ratio: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:TapChangerTablePoint.ratio'})
    x: Optional[PerCent] = field(default=None, metadata={'xpath': 'cim:TapChangerTablePoint.x'})
