from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from ...Core.IdentifiedObject import IdentifiedObject
from .LoadAggregate import LoadAggregate
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class LoadMotor(IdentifiedObject):
    d: Simple_Float = field(metadata={'xpath': 'cim:LoadMotor.d'})
    h: Seconds = field(metadata={'xpath': 'cim:LoadMotor.h'})
    lfac: Simple_Float = field(metadata={'xpath': 'cim:LoadMotor.lfac'})
    lp: PU = field(metadata={'xpath': 'cim:LoadMotor.lp'})
    lpp: PU = field(metadata={'xpath': 'cim:LoadMotor.lpp'})
    ls: PU = field(metadata={'xpath': 'cim:LoadMotor.ls'})
    pfrac: Simple_Float = field(metadata={'xpath': 'cim:LoadMotor.pfrac'})
    ra: PU = field(metadata={'xpath': 'cim:LoadMotor.ra'})
    tbkr: Seconds = field(metadata={'xpath': 'cim:LoadMotor.tbkr'})
    tpo: Seconds = field(metadata={'xpath': 'cim:LoadMotor.tpo'})
    tppo: Seconds = field(metadata={'xpath': 'cim:LoadMotor.tppo'})
    tv: Seconds = field(metadata={'xpath': 'cim:LoadMotor.tv'})
    vt: PU = field(metadata={'xpath': 'cim:LoadMotor.vt'})
    LoadAggregate_id: str | None = field(default=None, metadata={"xpath": "cim:LoadMotor.LoadAggregate/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    LoadAggregate_ref: LoadAggregate = None
