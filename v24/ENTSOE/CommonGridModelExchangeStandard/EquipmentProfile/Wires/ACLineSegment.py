from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Susceptance import Susceptance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Conductance import Conductance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Temperature import Temperature     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Reactance import Reactance     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.Conductor import Conductor

@dataclass
class ACLineSegment(Conductor):
    """A wire or combination of wires, with consistent electrical characteristics,
    building a single electrical system, used to carry alternating current between
    points in the power system.
      For symmetrical, transposed 3ph lines, it is sufficient to use  attributes of
    the line segment, which describe impedances and admittances for the entire
    length of the segment.  Additionally impedances can be computed by using length
    and associated per length impedances.
      The BaseVoltage at the two ends of ACLineSegments in a Line shall have the
    same BaseVoltage.nominalVoltage. However, boundary lines  may have slightly
    different BaseVoltage.nominalVoltages and  variation is allowed. Larger voltage
    difference in general requires use of an equivalent branch.
    """
    # Zero sequence shunt (charging) susceptance, uniformly distributed, of the
    # entire line section.
    b0ch: Susceptance  = None
 
    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the
    # entire line section.  This value represents the full charging over the full
    # length of the line.
    bch: Susceptance  = None
 
    # Zero sequence shunt (charging) conductance, uniformly distributed, of the
    # entire line section.
    g0ch: Conductance  = None
 
    # Positive sequence shunt (charging) conductance, uniformly distributed, of the
    # entire line section.
    gch: Conductance  = None
 
    # Positive sequence series resistance of the entire line section.
    r: Resistance  = None
 
    # Zero sequence series resistance of the entire line section.
    r0: Resistance  = None
 
    # Maximum permitted temperature at the end of SC for the calculation of minimum
    # short-circuit currents. Used for short circuit data exchange according to IEC
    # 60909
    shortCircuitEndTemperature: Temperature  = None
 
    # Positive sequence series reactance of the entire line section.
    x: Reactance  = None
 
    # Zero sequence series reactance of the entire line section.
    x0: Reactance  = None
     