from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.CurrentFlow import CurrentFlow     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.AngleDegrees import AngleDegrees     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.ConductingEquipment import ConductingEquipment

@dataclass
class PowerTransformer(ConductingEquipment):
    """An electrical device consisting of  two or more coupled windings, with or
    without a magnetic core, for introducing mutual coupling between electric
    circuits. Transformers can be used to control voltage and phase shift (active
    power flow).
      A power transformer may be composed of separate transformer tanks that need
    not be identical.
      A power transformer can be modeled with or without tanks and is intended for
    use in both balanced and unbalanced representations.   A power transformer
    typically has two terminals, but may have one (grounding), three or more
    terminals.
      The inherited association ConductingEquipment.BaseVoltage should not be used.
    The association from TransformerEnd to BaseVoltage should be used instead.
    """
    # The highest operating current (Ib in the IEC 60909-0) before short circuit
    # (depends on network configuration and relevant reliability philosophy). It is
    # used for calculation of the impedance correction factor KT defined in IEC 60909-
    # 0.
    beforeShCircuitHighestOperatingCurrent_: CurrentFlow  = None
 
    # The highest operating voltage (Ub in the IEC 60909-0) before short circuit. It
    # is used for calculation of the impedance correction factor KT defined in IEC
    # 60909-0. This is worst case voltage on the low side winding (Section 3.7.1 in
    # the standard). Used to define operating conditions.
    beforeShCircuitHighestOperatingVoltage_: Voltage  = None
 
    # The angle of power factor before short circuit (phib in the IEC 60909-0). It is
    # used for calculation of the impedance correction factor KT defined in IEC 60909-
    # 0. This is the worst case power factor. Used to define operating conditions.
    beforeShortCircuitAnglePf_: AngleDegrees  = None
 
    # The minimum operating voltage (uQmin in the IEC 60909-0) at the high voltage
    # side (Q side) of the unit transformer of the power station unit. A value well
    # established from long-term operating experience of the system. It is used for
    # calculation of the impedance correction factor KG defined in IEC 60909-0
    highSideMinOperatingU_: Voltage  = None
 
    # Indicates whether the machine is part of a power station unit. Used for short
    # circuit data exchange according to IEC 60909
    isPartOfGeneratorUnit_: bool  = None
 
    # It is used to define if the data (other attributes related to short circuit
    # data exchange) defines long term operational conditions or not. Used for short
    # circuit data exchange according to IEC 60909.
    operationalValuesConsidered_: bool  = None
     