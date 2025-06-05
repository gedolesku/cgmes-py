from __future__ import annotations
from ...DomainProfile.AngleDegrees import AngleDegrees
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.CurrentFlow import CurrentFlow
from ...DomainProfile.Voltage import Voltage
from ..Core.ConductingEquipment import ConductingEquipment
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class PowerTransformer(ConductingEquipment):
    isPartOfGeneratorUnit: Boolean = field(metadata={'xpath': 'cim:PowerTransformer.isPartOfGeneratorUnit'})
    beforeShCircuitHighestOperatingCurrent: Optional[CurrentFlow] = field(default=None, metadata={'xpath': 'cim:PowerTransformer.beforeShCircuitHighestOperatingCurrent'})
    beforeShCircuitHighestOperatingVoltage: Optional[Voltage] = field(default=None, metadata={'xpath': 'cim:PowerTransformer.beforeShCircuitHighestOperatingVoltage'})
    beforeShortCircuitAnglePf: Optional[AngleDegrees] = field(default=None, metadata={'xpath': 'cim:PowerTransformer.beforeShortCircuitAnglePf'})
    highSideMinOperatingU: Optional[Voltage] = field(default=None, metadata={'xpath': 'cim:PowerTransformer.highSideMinOperatingU'})
    operationalValuesConsidered: Optional[Boolean] = field(default=None, metadata={'xpath': 'cim:PowerTransformer.operationalValuesConsidered'})
