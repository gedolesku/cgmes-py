from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

@dataclass
class ShuntCompensator:
    """A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors.
    A section of a shunt compensator is an individual capacitor or reactor.  A
    negative value for reactivePerSection indicates that the compensator is a
    reactor. ShuntCompensator is a single terminal device.  Ground is implied.
    """
    pass
