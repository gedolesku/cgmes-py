from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class IfdBaseKind(Enum):
    """Excitation base system mode.
    """
    # Air gap line mode.  ifdBaseValue is computed, not defined by the user, in this
    # mode.
    ifag = auto()
    # No load system with saturation mode.  ifdBaseValue is computed, not defined by
    # the user, in this mode.
    ifnl = auto()
    # Full load system mode.  ifdBaseValue is computed, not defined by the user, in
    # this mode.
    iffl = auto()
    # Free mode.  ifdBaseValue is defined by the user in this mode.
    other = auto()