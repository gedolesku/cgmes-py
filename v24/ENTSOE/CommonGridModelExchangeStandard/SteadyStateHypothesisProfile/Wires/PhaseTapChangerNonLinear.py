from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.PhaseTapChanger import PhaseTapChanger

@dataclass
class PhaseTapChangerNonLinear(PhaseTapChanger):
    """The non-linear phase tap changer describes the non-linear behavior of a phase
    tap changer. This is a base class for the symmetrical and asymmetrical phase
    tap changer models. The details of these models can be found in the IEC 61970-
    301 document.
    """
    pass
