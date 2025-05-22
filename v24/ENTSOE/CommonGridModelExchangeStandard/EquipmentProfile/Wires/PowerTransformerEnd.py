from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Susceptance import Susceptance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.WindingConnection import WindingConnection     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ApparentPower import ApparentPower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Conductance import Conductance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Reactance import Reactance     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.TransformerEnd import TransformerEnd
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.PowerTransformer import PowerTransformer     

@dataclass
class PowerTransformerEnd(TransformerEnd):
    """A PowerTransformerEnd is associated with each Terminal of a PowerTransformer.
      The impedance values r, r0, x, and x0 of a PowerTransformerEnd represents a
    star equivalent as follows
      1) for a two Terminal PowerTransformer the high voltage PowerTransformerEnd
    has non zero values on r, r0, x, and x0 while the low voltage
    PowerTransformerEnd has zero values for r, r0, x, and x0.
      2) for a three Terminal PowerTransformer the three PowerTransformerEnds
    represents a star equivalent with each leg in the star represented by r, r0, x,
    and x0 values.
      3) for a PowerTransformer with more than three Terminals the
    PowerTransformerEnd impedance values cannot be used. Instead use the
    TransformerMeshImpedance or split the transformer into multiple
    PowerTransformers.
    """
    # Magnetizing branch susceptance (B mag).  The value can be positive or negative.
    b_: Susceptance  = None
 
    # Kind of connection.
    connectionKind_: WindingConnection  = None
 
    # Zero sequence magnetizing branch susceptance.
    b0_: Susceptance  = None
 
    # Terminal voltage phase angle displacement where 360 degrees are represented
    # with clock hours. The valid values are 0 to 11. For example, for the secondary
    # side end of a transformer with vector group code of 'Dyn11', specify the
    # connection kind as wye with neutral and specify the phase angle of the clock as
    # 11.  The clock value of the transformer end number specified as 1, is assumed
    # to be zero.  Note the transformer end number is not assumed to be the same as
    # the terminal sequence number.
    phaseAngleClock_: int  = None
 
    # Normal apparent power rating.
    # The attribute shall be a positive value. For a two-winding transformer the
    # values for the high and low voltage sides shall be identical. 
    ratedS_: ApparentPower  = None
 
    # Magnetizing branch conductance.
    g_: Conductance  = None
 
    # Rated voltage: phase-phase for three-phase windings, and either phase-phase or
    # phase-neutral for single-phase windings.
    # A high voltage side, as given by TransformerEnd.endNumber, shall have a ratedU
    # that is greater or equal than ratedU for the lower voltage sides.
    ratedU_: Voltage  = None
 
    # Zero sequence magnetizing branch conductance (star-model).
    g0_: Conductance  = None
 
    # Resistance (star-model) of the transformer end.
    # The attribute shall be equal or greater than zero for non-equivalent
    # transformers.
    r_: Resistance  = None
 
    # Zero sequence series resistance (star-model) of the transformer end.
    r0_: Resistance  = None
 
    # Positive sequence series reactance (star-model) of the transformer end.
    x_: Reactance  = None
 
    # Zero sequence series reactance of the transformer end.
    x0_: Reactance  = None
 
    # The ends of this power transformer.
    PowerTransformer_: Optional[PowerTransformer] = None
     