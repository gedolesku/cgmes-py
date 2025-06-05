from __future__ import annotations
from .Date import Date
from .String import String
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class DomainVersion(Protocol):
    baseUML: String  # metadata: cim='cim:DomainVersion.baseUML', mult='1'
    entsoeUML: String  # metadata: cim='cim:DomainVersion.entsoeUML', mult='1'
    version: String  # metadata: cim='cim:DomainVersion.version', mult='1'
    date: Optional[Date]  # metadata: cim='cim:DomainVersion.date', mult='0..1'
