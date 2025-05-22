from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

@dataclass
class DCEquipmentContainer:
    """A modeling construct to provide a root class for containment of DC as well as
    AC equipment. The class differ from the EquipmentContaner for AC in that it may
    also contain DCNodes. Hence it can contain both AC and DC equipment.
    """
    pass
