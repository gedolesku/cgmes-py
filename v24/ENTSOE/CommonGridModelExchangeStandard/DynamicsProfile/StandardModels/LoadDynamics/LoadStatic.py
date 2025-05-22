from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.LoadDynamics.StaticLoadModelKind import StaticLoadModelKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.LoadDynamics.LoadAggregate import LoadAggregate     

@dataclass
class LoadStatic(IdentifiedObject):
    """General static load model representing the sensitivity of the real and reactive
    power consumed by the load to the amplitude and frequency of the bus voltage.
    """
    # Type of static load model.  Typical Value = constantZ.
    staticLoadModelType_: StaticLoadModelKind  = None
 
    # First term voltage coefficient for active power (Kp1).  Not used when .
    # staticLoadModelType = constantZ.
    kp1_: Simple_Float  = None
 
    # Second term voltage coefficient for active power (Kp2).  Not used when .
    # staticLoadModelType = constantZ.
    kp2_: Simple_Float  = None
 
    # Third term voltage coefficient for active power (Kp3).  Not used when .
    # staticLoadModelType = constantZ.
    kp3_: Simple_Float  = None
 
    # Frequency coefficient for active power (Kp4).  Must be non-zero when .
    # staticLoadModelType = ZIP2.  Not used for all other values of .
    # staticLoadModelType.
    kp4_: Simple_Float  = None
 
    # First term voltage exponent for active power (Ep1).  Used only when .
    # staticLoadModelType = exponential.
    ep1_: Simple_Float  = None
 
    # Second term voltage exponent for active power (Ep2).  Used only when .
    # staticLoadModelType = exponential.
    ep2_: Simple_Float  = None
 
    # Third term voltage exponent for active power (Ep3).  Used only when .
    # staticLoadModelType = exponential.
    ep3_: Simple_Float  = None
 
    # Frequency deviation coefficient for active power (Kpf).  Not used when .
    # staticLoadModelType = constantZ.
    kpf_: Simple_Float  = None
 
    # First term voltage coefficient for reactive power (Kq1).  Not used when .
    # staticLoadModelType = constantZ.
    kq1_: Simple_Float  = None
 
    # Second term voltage coefficient for reactive power (Kq2).  Not used when .
    # staticLoadModelType = constantZ.
    kq2_: Simple_Float  = None
 
    # Third term voltage coefficient for reactive power (Kq3).  Not used when .
    # staticLoadModelType = constantZ.
    kq3_: Simple_Float  = None
 
    # Frequency coefficient for reactive power (Kq4).  Must be non-zero when .
    # staticLoadModelType = ZIP2.  Not used for all other values of .
    # staticLoadModelType.
    kq4_: Simple_Float  = None
 
    # First term voltage exponent for reactive power (Eq1).  Used only when .
    # staticLoadModelType = exponential.
    eq1_: Simple_Float  = None
 
    # Second term voltage exponent for reactive power (Eq2).  Used only when .
    # staticLoadModelType = exponential.
    eq2_: Simple_Float  = None
 
    # Third term voltage exponent for reactive power (Eq3).  Used only when .
    # staticLoadModelType = exponential.
    eq3_: Simple_Float  = None
 
    # Frequency deviation coefficient for reactive power (Kqf).  Not used when .
    # staticLoadModelType = constantZ.
    kqf_: Simple_Float  = None
 
    # Aggregate load to which this aggregate static load belongs.
    LoadAggregate_: Optional[LoadAggregate] = None
     