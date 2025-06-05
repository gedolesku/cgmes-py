from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class DiscExcContIEEEDEC1A(DiscontinuousExcitationControlDynamics):
    esc: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.esc'})
    kan: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.kan'})
    ketl: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.ketl'})
    tan: Seconds = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.tan'})
    td: Seconds = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.td'})
    tl1: Seconds = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.tl1'})
    tl2: Seconds = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.tl2'})
    tw5: Seconds = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.tw5'})
    val: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.val'})
    vanmax: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.vanmax'})
    vomax: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.vomax'})
    vomin: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.vomin'})
    vsmax: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.vsmax'})
    vsmin: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.vsmin'})
    vtc: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.vtc'})
    vtlmt: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.vtlmt'})
    vtm: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.vtm'})
    vtn: PU = field(metadata={'xpath': 'cim:DiscExcContIEEEDEC1A.vtn'})
