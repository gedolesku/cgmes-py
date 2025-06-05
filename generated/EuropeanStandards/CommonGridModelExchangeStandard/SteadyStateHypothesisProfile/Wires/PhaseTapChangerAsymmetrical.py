from __future__ import annotations
from .PhaseTapChangerNonLinear import PhaseTapChangerNonLinear
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class PhaseTapChangerAsymmetrical(PhaseTapChangerNonLinear):
    pass
