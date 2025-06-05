from __future__ import annotations
from ..CommonGridModelExchangeStandard.DomainProfile.Date import Date
from ..CommonGridModelExchangeStandard.DomainProfile.String import String
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class ExtensionVersion(Protocol):
    namespaceURI: String  # metadata: cim='cim:ExtensionVersion.namespaceURI', mult='1'
    date: Optional[Date]  # metadata: cim='cim:ExtensionVersion.date', mult='0..1'
