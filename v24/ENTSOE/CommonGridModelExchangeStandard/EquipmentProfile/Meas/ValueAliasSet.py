from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class ValueAliasSet(IdentifiedObject):
    """Describes the translation of a set of values into a name and is intendend to
    facilitate cusom translations. Each ValueAliasSet has a name, description etc.
    A specific Measurement may represent a discrete state like Open, Closed,
    Intermediate etc. This requires a translation from the MeasurementValue.value
    number to a string, e.g. 0->"Invalid", 1->"Open", 2->"Closed", 3-
    >"Intermediate". Each ValueToAlias member in ValueAliasSet.Value describe a
    mapping for one particular value to a name.
    """
    pass
