from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto

class DroopSignalFeedbackKind(Enum):
    """Governor droop signal feedback source.
    """
    # Electrical power feedback (connection indicated as 1 in the block diagrams of
    # models, e.g. GovCT1, GovCT2).
    electricalPower = auto()
    # No droop signal feedback, is isochronous governor.
    none = auto()
    # Fuel valve stroke feedback (true stroke) (connection indicated as 2 in the
    # block diagrams of model, e.g. GovCT1, GovCT2).
    fuelValveStroke = auto()
    # Governor output feedback (requested stroke) (connection indicated as 3 in the
    # block diagrams of models, e.g. GovCT1, GovCT2).
    governorOutput = auto()