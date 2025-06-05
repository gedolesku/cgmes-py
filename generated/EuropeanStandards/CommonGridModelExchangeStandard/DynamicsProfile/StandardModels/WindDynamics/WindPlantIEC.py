from __future__ import annotations
from .WindPlantDynamics import WindPlantDynamics
from .WindPlantFreqPcontrolIEC import WindPlantFreqPcontrolIEC
from .WindPlantReactiveControlIEC import WindPlantReactiveControlIEC
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindPlantIEC(WindPlantDynamics):
    WindPlantFreqPcontrolIEC_id: str | None = field(default=None, metadata={"xpath": "cim:WindPlantIEC.WindPlantFreqPcontrolIEC/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    WindPlantFreqPcontrolIEC_ref: WindPlantFreqPcontrolIEC = None
    WindPlantReactiveControlIEC_id: str | None = field(default=None, metadata={"xpath": "cim:WindPlantIEC.WindPlantReactiveControlIEC/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    WindPlantReactiveControlIEC_ref: WindPlantReactiveControlIEC = None
