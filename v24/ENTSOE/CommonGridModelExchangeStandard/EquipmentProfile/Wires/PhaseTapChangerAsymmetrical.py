from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.AngleDegrees import AngleDegrees     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.PhaseTapChangerNonLinear import PhaseTapChangerNonLinear

@dataclass
class PhaseTapChangerAsymmetrical(PhaseTapChangerNonLinear):
    """Describes the tap model for an asymmetrical phase shifting transformer in which
    the difference voltage vector adds to the primary side voltage. The angle
    between the primary side voltage and the difference voltage is named the
    winding connection angle. The phase shift depends on both the difference
    voltage magnitude and the winding connection angle.
    """
    # The phase angle between the in-phase winding and the out-of -phase winding used
    # for creating phase shift. The out-of-phase winding produces what is known as
    # the difference voltage.  Setting this angle to 90 degrees is not the same as a
    # symmemtrical transformer.
    windingConnectionAngle: AngleDegrees  = None
     