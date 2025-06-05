from __future__ import annotations
from ...DomainProfile.AngleDegrees import AngleDegrees
from ...DomainProfile.CurrentFlow import CurrentFlow
from .ACDCConverter import ACDCConverter
from .CsOperatingModeKind import CsOperatingModeKind
from .CsPpccControlKind import CsPpccControlKind
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class CsConverter(ACDCConverter):
    operatingMode: CsOperatingModeKind = field(metadata={'xpath': 'cim:CsConverter.operatingMode'})
    pPccControl: CsPpccControlKind = field(metadata={'xpath': 'cim:CsConverter.pPccControl'})
    targetAlpha: AngleDegrees = field(metadata={'xpath': 'cim:CsConverter.targetAlpha'})
    targetGamma: AngleDegrees = field(metadata={'xpath': 'cim:CsConverter.targetGamma'})
    targetIdc: CurrentFlow = field(metadata={'xpath': 'cim:CsConverter.targetIdc'})
