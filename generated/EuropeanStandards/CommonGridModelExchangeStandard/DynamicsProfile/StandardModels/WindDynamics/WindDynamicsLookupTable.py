from __future__ import annotations
from ....DomainProfile.Integer import Integer
from ....DomainProfile.Simple_Float import Simple_Float
from ...Core.IdentifiedObject import IdentifiedObject
from .WindContCurrLimIEC import WindContCurrLimIEC
from .WindContPType3IEC import WindContPType3IEC
from .WindContRotorRIEC import WindContRotorRIEC
from .WindLookupTableFunctionKind import WindLookupTableFunctionKind
from .WindPlantFreqPcontrolIEC import WindPlantFreqPcontrolIEC
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class WindDynamicsLookupTable(IdentifiedObject):
    input: Simple_Float = field(metadata={'xpath': 'cim:WindDynamicsLookupTable.input'})
    lookupTableFunctionType: WindLookupTableFunctionKind = field(metadata={'xpath': 'cim:WindDynamicsLookupTable.lookupTableFunctionType'})
    output: Simple_Float = field(metadata={'xpath': 'cim:WindDynamicsLookupTable.output'})
    sequence: Integer = field(metadata={'xpath': 'cim:WindDynamicsLookupTable.sequence'})
    WindContRotorRIEC_id: str | None = field(default=None, metadata={"xpath": "cim:WindDynamicsLookupTable.WindContRotorRIEC/@rdf:resource", "pattern": r"^#.+$"})
    WindContRotorRIEC_ref: WindContRotorRIEC | None = None
    WindContCurrLimIEC_id: str | None = field(default=None, metadata={"xpath": "cim:WindDynamicsLookupTable.WindContCurrLimIEC/@rdf:resource", "pattern": r"^#.+$"})
    WindContCurrLimIEC_ref: WindContCurrLimIEC | None = None
    WindPlantFreqPcontrolIEC_id: str | None = field(default=None, metadata={"xpath": "cim:WindDynamicsLookupTable.WindPlantFreqPcontrolIEC/@rdf:resource", "pattern": r"^#.+$"})
    WindPlantFreqPcontrolIEC_ref: WindPlantFreqPcontrolIEC | None = None
    WindContPType3IEC_id: str | None = field(default=None, metadata={"xpath": "cim:WindDynamicsLookupTable.WindContPType3IEC/@rdf:resource", "pattern": r"^#.+$"})
    WindContPType3IEC_ref: WindContPType3IEC | None = None
