from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ...DomainProfile.Money import Money
from ...DomainProfile.PerCent import PerCent
from ...DomainProfile.Simple_Float import Simple_Float
from ..Core.Equipment import Equipment
from .GeneratorControlSource import GeneratorControlSource
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class GeneratingUnit(Equipment):
    initialP: ActivePower = field(metadata={'xpath': 'cim:GeneratingUnit.initialP'})
    maxOperatingP: ActivePower = field(metadata={'xpath': 'cim:GeneratingUnit.maxOperatingP'})
    minOperatingP: ActivePower = field(metadata={'xpath': 'cim:GeneratingUnit.minOperatingP'})
    genControlSource: Optional[GeneratorControlSource] = field(default=None, metadata={'xpath': 'cim:GeneratingUnit.genControlSource'})
    governorSCD: Optional[PerCent] = field(default=None, metadata={'xpath': 'cim:GeneratingUnit.governorSCD'})
    longPF: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:GeneratingUnit.longPF'})
    maximumAllowableSpinningReserve: Optional[ActivePower] = field(default=None, metadata={'xpath': 'cim:GeneratingUnit.maximumAllowableSpinningReserve'})
    nominalP: Optional[ActivePower] = field(default=None, metadata={'xpath': 'cim:GeneratingUnit.nominalP'})
    ratedGrossMaxP: Optional[ActivePower] = field(default=None, metadata={'xpath': 'cim:GeneratingUnit.ratedGrossMaxP'})
    ratedGrossMinP: Optional[ActivePower] = field(default=None, metadata={'xpath': 'cim:GeneratingUnit.ratedGrossMinP'})
    ratedNetMaxP: Optional[ActivePower] = field(default=None, metadata={'xpath': 'cim:GeneratingUnit.ratedNetMaxP'})
    shortPF: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:GeneratingUnit.shortPF'})
    startupCost: Optional[Money] = field(default=None, metadata={'xpath': 'cim:GeneratingUnit.startupCost'})
    totalEfficiency: Optional[PerCent] = field(default=None, metadata={'xpath': 'cim:GeneratingUnit.totalEfficiency'})
    variableCost: Optional[Money] = field(default=None, metadata={'xpath': 'cim:GeneratingUnit.variableCost'})
