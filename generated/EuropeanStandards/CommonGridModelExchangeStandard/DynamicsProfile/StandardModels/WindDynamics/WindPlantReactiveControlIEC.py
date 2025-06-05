from __future__ import annotations
from ....DomainProfile.Boolean import Boolean
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from ....DomainProfile.Simple_Float import Simple_Float
from ...Core.IdentifiedObject import IdentifiedObject
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class WindPlantReactiveControlIEC(IdentifiedObject):
    kiwpx: Simple_Float = field(metadata={'xpath': 'cim:WindPlantReactiveControlIEC.kiwpx'})
    kpwpx: Simple_Float = field(metadata={'xpath': 'cim:WindPlantReactiveControlIEC.kpwpx'})
    kwpqu: PU = field(metadata={'xpath': 'cim:WindPlantReactiveControlIEC.kwpqu'})
    mwppf: Boolean = field(metadata={'xpath': 'cim:WindPlantReactiveControlIEC.mwppf'})
    mwpu: Boolean = field(metadata={'xpath': 'cim:WindPlantReactiveControlIEC.mwpu'})
    twppfilt: Seconds = field(metadata={'xpath': 'cim:WindPlantReactiveControlIEC.twppfilt'})
    twpqfilt: Seconds = field(metadata={'xpath': 'cim:WindPlantReactiveControlIEC.twpqfilt'})
    twpufilt: Seconds = field(metadata={'xpath': 'cim:WindPlantReactiveControlIEC.twpufilt'})
    txft: Seconds = field(metadata={'xpath': 'cim:WindPlantReactiveControlIEC.txft'})
    txfv: Seconds = field(metadata={'xpath': 'cim:WindPlantReactiveControlIEC.txfv'})
    uwpqdip: PU = field(metadata={'xpath': 'cim:WindPlantReactiveControlIEC.uwpqdip'})
    xrefmax: PU = field(metadata={'xpath': 'cim:WindPlantReactiveControlIEC.xrefmax'})
    xrefmin: PU = field(metadata={'xpath': 'cim:WindPlantReactiveControlIEC.xrefmin'})
