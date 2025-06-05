from __future__ import annotations
from ...DomainProfile.Reactance import Reactance
from ...DomainProfile.Resistance import Resistance
from .EquivalentEquipment import EquivalentEquipment
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class EquivalentBranch(EquivalentEquipment):
    negativeR12: Resistance = field(metadata={'xpath': 'cim:EquivalentBranch.negativeR12'})
    negativeR21: Resistance = field(metadata={'xpath': 'cim:EquivalentBranch.negativeR21'})
    negativeX12: Reactance = field(metadata={'xpath': 'cim:EquivalentBranch.negativeX12'})
    negativeX21: Reactance = field(metadata={'xpath': 'cim:EquivalentBranch.negativeX21'})
    positiveR12: Resistance = field(metadata={'xpath': 'cim:EquivalentBranch.positiveR12'})
    positiveR21: Resistance = field(metadata={'xpath': 'cim:EquivalentBranch.positiveR21'})
    positiveX12: Reactance = field(metadata={'xpath': 'cim:EquivalentBranch.positiveX12'})
    positiveX21: Reactance = field(metadata={'xpath': 'cim:EquivalentBranch.positiveX21'})
    r: Resistance = field(metadata={'xpath': 'cim:EquivalentBranch.r'})
    x: Reactance = field(metadata={'xpath': 'cim:EquivalentBranch.x'})
    zeroR12: Resistance = field(metadata={'xpath': 'cim:EquivalentBranch.zeroR12'})
    zeroR21: Resistance = field(metadata={'xpath': 'cim:EquivalentBranch.zeroR21'})
    zeroX12: Reactance = field(metadata={'xpath': 'cim:EquivalentBranch.zeroX12'})
    zeroX21: Reactance = field(metadata={'xpath': 'cim:EquivalentBranch.zeroX21'})
    r21: Optional[Resistance] = field(default=None, metadata={'xpath': 'cim:EquivalentBranch.r21'})
    x21: Optional[Reactance] = field(default=None, metadata={'xpath': 'cim:EquivalentBranch.x21'})
