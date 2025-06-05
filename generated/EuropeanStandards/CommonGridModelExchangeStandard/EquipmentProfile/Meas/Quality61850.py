from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from .Source import Source
from .Validity import Validity
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class Quality61850(Protocol):
    badReference: Optional[Boolean]  # metadata: cim='cim:Quality61850.badReference', mult='0..1'
    estimatorReplaced: Optional[Boolean]  # metadata: cim='cim:Quality61850.estimatorReplaced', mult='0..1'
    failure: Optional[Boolean]  # metadata: cim='cim:Quality61850.failure', mult='0..1'
    oldData: Optional[Boolean]  # metadata: cim='cim:Quality61850.oldData', mult='0..1'
    operatorBlocked: Optional[Boolean]  # metadata: cim='cim:Quality61850.operatorBlocked', mult='0..1'
    oscillatory: Optional[Boolean]  # metadata: cim='cim:Quality61850.oscillatory', mult='0..1'
    outOfRange: Optional[Boolean]  # metadata: cim='cim:Quality61850.outOfRange', mult='0..1'
    overFlow: Optional[Boolean]  # metadata: cim='cim:Quality61850.overFlow', mult='0..1'
    source: Optional[Source]  # metadata: cim='cim:Quality61850.source', mult='0..1'
    suspect: Optional[Boolean]  # metadata: cim='cim:Quality61850.suspect', mult='0..1'
    test: Optional[Boolean]  # metadata: cim='cim:Quality61850.test', mult='0..1'
    validity: Optional[Validity]  # metadata: cim='cim:Quality61850.validity', mult='0..1'
