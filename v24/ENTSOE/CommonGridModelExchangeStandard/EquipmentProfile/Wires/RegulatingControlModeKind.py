from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class RegulatingControlModeKind(Enum):
    """The kind of regulation model.   For example regulating voltage, reactive power,
    active power, etc.
    """
    # Voltage is specified.
    voltage = auto()
    # Active power is specified.
    activePower = auto()
    # Reactive power is specified.
    reactivePower = auto()
    # Current flow is specified.
    currentFlow = auto()
    # Admittance is specified.
    admittance = auto()
    # Control switches on/off by time of day. The times may change on the weekend, or
    # in different seasons.
    timeScheduled = auto()
    # Control switches on/off based on the local temperature (i.e., a thermostat).
    temperature = auto()
    # Power factor is specified.
    powerFactor = auto()