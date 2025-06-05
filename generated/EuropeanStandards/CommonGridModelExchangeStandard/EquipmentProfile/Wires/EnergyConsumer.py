from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ...DomainProfile.PerCent import PerCent
from ...DomainProfile.ReactivePower import ReactivePower
from ..Core.ConductingEquipment import ConductingEquipment
from ..LoadModel.LoadResponseCharacteristic import LoadResponseCharacteristic
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class EnergyConsumer(ConductingEquipment):
    pfixed: Optional[ActivePower] = field(default=None, metadata={'xpath': 'cim:EnergyConsumer.pfixed'})
    pfixedPct: Optional[PerCent] = field(default=None, metadata={'xpath': 'cim:EnergyConsumer.pfixedPct'})
    qfixed: Optional[ReactivePower] = field(default=None, metadata={'xpath': 'cim:EnergyConsumer.qfixed'})
    qfixedPct: Optional[PerCent] = field(default=None, metadata={'xpath': 'cim:EnergyConsumer.qfixedPct'})
    LoadResponse_id: str | None = field(default=None, metadata={"xpath": "cim:EnergyConsumer.LoadResponse/@rdf:resource", "pattern": r"^#.+$"})
    LoadResponse_ref: LoadResponseCharacteristic | None = None
