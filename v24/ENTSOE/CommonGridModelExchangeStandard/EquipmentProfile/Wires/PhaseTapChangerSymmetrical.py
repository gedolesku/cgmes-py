from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.PhaseTapChangerNonLinear import PhaseTapChangerNonLinear

@dataclass
class PhaseTapChangerSymmetrical(PhaseTapChangerNonLinear):
    """Describes a symmetrical phase shifting transformer tap model in which the
    secondary side voltage magnitude is the same as at the primary side. The
    difference voltage magnitude is the base in an equal-sided triangle where the
    sides corresponds to the primary and secondary voltages. The phase angle
    difference corresponds to the top angle and can be expressed as twice the
    arctangent of half the total difference voltage.
    """
    pass
