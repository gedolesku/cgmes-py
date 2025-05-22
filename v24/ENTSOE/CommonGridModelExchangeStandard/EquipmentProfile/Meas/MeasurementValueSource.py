from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class MeasurementValueSource(IdentifiedObject):
    """MeasurementValueSource describes the alternative sources updating a
    MeasurementValue. User conventions for how to use the MeasurementValueSource
    attributes are described in the introduction to IEC 61970-301.
    """
    pass
