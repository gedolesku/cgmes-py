from __future__ import annotations
from ...DomainProfile.ApparentPower import ApparentPower
from ...DomainProfile.Conductance import Conductance
from ...DomainProfile.Integer import Integer
from ...DomainProfile.Reactance import Reactance
from ...DomainProfile.Resistance import Resistance
from ...DomainProfile.Susceptance import Susceptance
from ...DomainProfile.Voltage import Voltage
from .PowerTransformer import PowerTransformer
from .TransformerEnd import TransformerEnd
from .WindingConnection import WindingConnection
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class PowerTransformerEnd(TransformerEnd):
    b: Susceptance = field(metadata={'xpath': 'cim:PowerTransformerEnd.b'})
    b0: Susceptance = field(metadata={'xpath': 'cim:PowerTransformerEnd.b0'})
    g0: Conductance = field(metadata={'xpath': 'cim:PowerTransformerEnd.g0'})
    phaseAngleClock: Integer = field(metadata={'xpath': 'cim:PowerTransformerEnd.phaseAngleClock'})
    r: Resistance = field(metadata={'xpath': 'cim:PowerTransformerEnd.r'})
    r0: Resistance = field(metadata={'xpath': 'cim:PowerTransformerEnd.r0'})
    ratedU: Voltage = field(metadata={'xpath': 'cim:PowerTransformerEnd.ratedU'})
    x: Reactance = field(metadata={'xpath': 'cim:PowerTransformerEnd.x'})
    x0: Reactance = field(metadata={'xpath': 'cim:PowerTransformerEnd.x0'})
    PowerTransformer_id: str | None = field(default=None, metadata={"xpath": "cim:PowerTransformerEnd.PowerTransformer/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    PowerTransformer_ref: PowerTransformer = None
    connectionKind: Optional[WindingConnection] = field(default=None, metadata={'xpath': 'cim:PowerTransformerEnd.connectionKind'})
    g: Optional[Conductance] = field(default=None, metadata={'xpath': 'cim:PowerTransformerEnd.g'})
    ratedS: Optional[ApparentPower] = field(default=None, metadata={'xpath': 'cim:PowerTransformerEnd.ratedS'})
