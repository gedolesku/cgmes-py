from __future__ import annotations
from ...StateVariablesProfile.Core.ACDCTerminal import ACDCTerminal
from typing import Protocol, runtime_checkable
# pylint: disable=function-redefined

@runtime_checkable
class ACDCTerminal(ACDCTerminal, Protocol):
    pass
