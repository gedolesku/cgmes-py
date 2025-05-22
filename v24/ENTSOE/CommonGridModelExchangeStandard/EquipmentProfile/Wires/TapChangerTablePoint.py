from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PerCent import PerCent     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     

@dataclass
class TapChangerTablePoint:
    # The magnetizing branch susceptance deviation in percent of nominal value. The
    # actual susceptance is calculated as follows:
    # calculated magnetizing susceptance = b(nominal) * (1 + b(from this class)/100).
    #  The b(nominal) is defined as the static magnetizing susceptance on the
    # associated power transformer end or ends.  This model assumes the star
    # impedance (pi model) form.
    b_: PerCent  = None
 
    # The magnetizing branch conductance deviation in percent of nominal value. The
    # actual conductance is calculated as follows:
    # calculated magnetizing conductance = g(nominal) * (1 + g(from this class)/100).
    #  The g(nominal) is defined as the static magnetizing conductance on the
    # associated power transformer end or ends.  This model assumes the star
    # impedance (pi model) form.
    g_: PerCent  = None
 
    # The resistance deviation in percent of nominal value. The actual reactance is
    # calculated as follows:
    # calculated resistance = r(nominal) * (1 + r(from this class)/100).   The
    # r(nominal) is defined as the static resistance on the associated power
    # transformer end or ends.  This model assumes the star impedance (pi model) form.
    r_: PerCent  = None
 
    # The voltage ratio in per unit. Hence this is a value close to one.
    ratio_: Simple_Float  = None
 
    # The tap step.
    step_: int  = None
 
    # The series reactance deviation in percent of nominal value. The actual
    # reactance is calculated as follows:
    # calculated reactance = x(nominal) * (1 + x(from this class)/100).   The
    # x(nominal) is defined as the static series reactance on the associated power
    # transformer end or ends.  This model assumes the star impedance (pi model) form.
    x_: PerCent  = None
     