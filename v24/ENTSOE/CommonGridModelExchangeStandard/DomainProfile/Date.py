from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

@dataclass
class Date:
    """Date as "yyyy-mm-dd", which conforms with ISO 8601. UTC time zone is specified
    as "yyyy-mm-ddZ". A local timezone relative UTC is specified as "yyyy-mm-dd(+/-
    )hh:mm".
    """
    pass
