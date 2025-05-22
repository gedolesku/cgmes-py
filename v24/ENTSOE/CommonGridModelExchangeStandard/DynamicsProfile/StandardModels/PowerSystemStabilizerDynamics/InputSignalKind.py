from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class InputSignalKind(Enum):
    """Input signal type.  In Dynamics modelling, commonly represented by j parameter.
    """
    # Input signal is rotor or shaft speed (angular frequency).
    rotorSpeed = auto()
    # Input signal is rotor or shaft angular frequency deviation.
    rotorAngularFrequencyDeviation = auto()
    # Input signal is bus voltage fr<font color="#0f0f0f">equency.  This could be a
    # terminal frequency or remote frequency.</font>
    busFrequency = auto()
    # Input signal is deviation of bus voltage frequ<font color="#0f0f0f">ency.  This
    # could be a terminal frequency deviation or remote frequency deviation.</font>
    busFrequencyDeviation = auto()
    # Input signal is generator electrical power on rated S.
    generatorElectricalPower = auto()
    # Input signal is generating accelerating power.
    generatorAcceleratingPower = auto()
    # Input signal <font color="#0f0f0f">is bus voltage.  This could be a terminal
    # voltage or remote voltage.</font>
    busVoltage = auto()
    # Input signal is derivative of bus voltag<font color="#0f0f0f">e.  This could be
    # a terminal voltage derivative or remote voltage derivative.</font>
    busVoltageDerivative = auto()
    # Input signal is amplitude of remote branch current.
    branchCurrent = auto()
    # Input signal is generator field current.
    fieldCurrent = auto()