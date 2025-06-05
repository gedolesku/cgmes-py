from __future__ import annotations
from ...DomainProfile.AngleDegrees import AngleDegrees
from ...DomainProfile.CurrentFlow import CurrentFlow
from .ACDCConverter import ACDCConverter
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class CsConverter(ACDCConverter):
    maxAlpha: Optional[AngleDegrees] = field(default=None, metadata={'xpath': 'cim:CsConverter.maxAlpha'})
    maxGamma: Optional[AngleDegrees] = field(default=None, metadata={'xpath': 'cim:CsConverter.maxGamma'})
    maxIdc: Optional[CurrentFlow] = field(default=None, metadata={'xpath': 'cim:CsConverter.maxIdc'})
    minAlpha: Optional[AngleDegrees] = field(default=None, metadata={'xpath': 'cim:CsConverter.minAlpha'})
    minGamma: Optional[AngleDegrees] = field(default=None, metadata={'xpath': 'cim:CsConverter.minGamma'})
    minIdc: Optional[CurrentFlow] = field(default=None, metadata={'xpath': 'cim:CsConverter.minIdc'})
    ratedIdc: Optional[CurrentFlow] = field(default=None, metadata={'xpath': 'cim:CsConverter.ratedIdc'})
