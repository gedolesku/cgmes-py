from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class Source(Enum):
    """Source gives information related to the origin of a value.
    """
    # The value is provided by input from the process I/O or being calculated from
    # some function.
    PROCESS = auto()
    # The value contains a default value.
    DEFAULTED = auto()
    # The value is provided by input of an operator or by an automatic source.
    SUBSTITUTED = auto()