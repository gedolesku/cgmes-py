from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.PhaseTapChangerNonLinear import PhaseTapChangerNonLinear

@dataclass
class PhaseTapChangerAsymmetrical(PhaseTapChangerNonLinear):
    """Describes the tap model for an asymmetrical phase shifting transformer in which
    the difference voltage vector adds to the primary side voltage. The angle
    between the primary side voltage and the difference voltage is named the
    winding connection angle. The phase shift depends on both the difference
    voltage magnitude and the winding connection angle.
    """
    pass
