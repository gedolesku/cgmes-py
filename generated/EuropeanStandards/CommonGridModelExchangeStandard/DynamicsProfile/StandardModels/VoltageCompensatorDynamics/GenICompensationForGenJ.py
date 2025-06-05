from __future__ import annotations
from ....DomainProfile.PU import PU
from ...Core.IdentifiedObject import IdentifiedObject
from ..SynchronousMachineDynamics.SynchronousMachineDynamics import SynchronousMachineDynamics
from .VCompIEEEType2 import VCompIEEEType2
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class GenICompensationForGenJ(IdentifiedObject):
    rcij: PU = field(metadata={'xpath': 'cim:GenICompensationForGenJ.rcij'})
    xcij: PU = field(metadata={'xpath': 'cim:GenICompensationForGenJ.xcij'})
    SynchronousMachineDynamics_id: str | None = field(default=None, metadata={"xpath": "cim:GenICompensationForGenJ.SynchronousMachineDynamics/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    SynchronousMachineDynamics_ref: SynchronousMachineDynamics = None
    VcompIEEEType2_id: str | None = field(default=None, metadata={"xpath": "cim:GenICompensationForGenJ.VcompIEEEType2/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    VcompIEEEType2_ref: VCompIEEEType2 = None
