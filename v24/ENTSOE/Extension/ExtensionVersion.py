from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:
    from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Date import Date
if TYPE_CHECKING:
    from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.String import String

@dataclass
class ExtensionVersion:
    """Version details."""

    # Profile creation date
    # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.
    date: str = "2014-08-07"

    # ENTSO-E namespace URI. The last two elements in the URI (http://entsoe.eu/CIM/SchemaExtension/yy/zzz#) indicate major and minor versions where:
    # - yy - indicates a major version;
    # - zzz - indicates a minor version.
    namespaceURI: str = "http://entsoe.eu/CIM/SchemaExtension/3/1#"

