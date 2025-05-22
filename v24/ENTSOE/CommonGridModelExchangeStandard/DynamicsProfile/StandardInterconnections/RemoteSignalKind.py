from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class RemoteSignalKind(Enum):
    """Type of input signal coming from remote bus.
    """
    # Input is voltage frequency from remote terminal bus.
    remoteBusVoltageFrequency = auto()
    # Input is voltage frequency deviation from remote terminal bus.
    remoteBusVoltageFrequencyDeviation = auto()
    # Input is frequency from remote terminal bus.
    remoteBusFrequency = auto()
    # Input is frequency deviation from remote terminal bus.
    remoteBusFrequencyDeviation = auto()
    # Input is voltage amplitude from remote terminal bus.
    remoteBusVoltageAmplitude = auto()
    # Input is voltage from remote terminal bus.
    remoteBusVoltage = auto()
    # Input is branch current amplitude from remote terminal bus.
    remoteBranchCurrentAmplitude = auto()
    # Input is branch current amplitude derivative from remote terminal bus.
    remoteBusVoltageAmplitudeDerivative = auto()
    # Input is PU voltage derivative from remote terminal bus.
    remotePuBusVoltageDerivative = auto()