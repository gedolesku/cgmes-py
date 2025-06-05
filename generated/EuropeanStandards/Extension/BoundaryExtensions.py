from __future__ import annotations
from ..CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean
from ..CommonGridModelExchangeStandard.DomainProfile.String import String
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class BoundaryExtensions:
    boundaryPoint: Optional[Boolean] = field(default=None, metadata={'xpath': 'cim:BoundaryExtensions.boundaryPoint'})
    fromEndIsoCode: Optional[String] = field(default=None, metadata={'xpath': 'cim:BoundaryExtensions.fromEndIsoCode'})
    fromEndName: Optional[String] = field(default=None, metadata={'xpath': 'cim:BoundaryExtensions.fromEndName'})
    fromEndNameTso: Optional[String] = field(default=None, metadata={'xpath': 'cim:BoundaryExtensions.fromEndNameTso'})
    toEndIsoCode: Optional[String] = field(default=None, metadata={'xpath': 'cim:BoundaryExtensions.toEndIsoCode'})
    toEndName: Optional[String] = field(default=None, metadata={'xpath': 'cim:BoundaryExtensions.toEndName'})
    toEndNameTso: Optional[String] = field(default=None, metadata={'xpath': 'cim:BoundaryExtensions.toEndNameTso'})
