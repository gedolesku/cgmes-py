from __future__ import annotations
from ..Core.IdentifiedObject import IdentifiedObject
from ..Core.Terminal import Terminal
from ..StandardModels.DiscontinuousExcitationControlDynamics.DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics
from ..StandardModels.PFVArControllerType1Dynamics.PFVArControllerType1Dynamics import PFVArControllerType1Dynamics
from ..StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from ..StandardModels.UnderexcitationLimiterDynamics.UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics
from ..StandardModels.VoltageCompensatorDynamics.VoltageCompensatorDynamics import VoltageCompensatorDynamics
from .RemoteSignalKind import RemoteSignalKind
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class RemoteInputSignal(IdentifiedObject):
    remoteSignalType: RemoteSignalKind = field(metadata={'xpath': 'cim:RemoteInputSignal.remoteSignalType'})
    Terminal_id: str | None = field(default=None, metadata={"xpath": "cim:RemoteInputSignal.Terminal/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    Terminal_ref: Terminal = None
    DiscontinuousExcitationControlDynamics_id: str | None = field(default=None, metadata={"xpath": "cim:RemoteInputSignal.DiscontinuousExcitationControlDynamics/@rdf:resource", "pattern": r"^#.+$"})
    DiscontinuousExcitationControlDynamics_ref: DiscontinuousExcitationControlDynamics | None = None
    PowerSystemStabilizerDynamics_id: str | None = field(default=None, metadata={"xpath": "cim:RemoteInputSignal.PowerSystemStabilizerDynamics/@rdf:resource", "pattern": r"^#.+$"})
    PowerSystemStabilizerDynamics_ref: PowerSystemStabilizerDynamics | None = None
    VoltageCompensatorDynamics_id: str | None = field(default=None, metadata={"xpath": "cim:RemoteInputSignal.VoltageCompensatorDynamics/@rdf:resource", "pattern": r"^#.+$"})
    VoltageCompensatorDynamics_ref: VoltageCompensatorDynamics | None = None
    UnderexcitationLimiterDynamics_id: str | None = field(default=None, metadata={"xpath": "cim:RemoteInputSignal.UnderexcitationLimiterDynamics/@rdf:resource", "pattern": r"^#.+$"})
    UnderexcitationLimiterDynamics_ref: UnderexcitationLimiterDynamics | None = None
    PFVArControllerType1Dynamics_id: str | None = field(default=None, metadata={"xpath": "cim:RemoteInputSignal.PFVArControllerType1Dynamics/@rdf:resource", "pattern": r"^#.+$"})
    PFVArControllerType1Dynamics_ref: PFVArControllerType1Dynamics | None = None
