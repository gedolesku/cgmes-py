from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from ...Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindPlantFreqPcontrolIEC(IdentifiedObject):
    dprefmax: PU = field(metadata={'xpath': 'cim:WindPlantFreqPcontrolIEC.dprefmax'})
    dprefmin: PU = field(metadata={'xpath': 'cim:WindPlantFreqPcontrolIEC.dprefmin'})
    kiwpp: Simple_Float = field(metadata={'xpath': 'cim:WindPlantFreqPcontrolIEC.kiwpp'})
    kpwpp: Simple_Float = field(metadata={'xpath': 'cim:WindPlantFreqPcontrolIEC.kpwpp'})
    prefmax: PU = field(metadata={'xpath': 'cim:WindPlantFreqPcontrolIEC.prefmax'})
    prefmin: PU = field(metadata={'xpath': 'cim:WindPlantFreqPcontrolIEC.prefmin'})
    tpft: Seconds = field(metadata={'xpath': 'cim:WindPlantFreqPcontrolIEC.tpft'})
    tpfv: Seconds = field(metadata={'xpath': 'cim:WindPlantFreqPcontrolIEC.tpfv'})
    twpffilt: Seconds = field(metadata={'xpath': 'cim:WindPlantFreqPcontrolIEC.twpffilt'})
    twppfilt: Seconds = field(metadata={'xpath': 'cim:WindPlantFreqPcontrolIEC.twppfilt'})
