from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Reactance import Reactance     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Equivalents.EquivalentEquipment import EquivalentEquipment

@dataclass
class EquivalentBranch(EquivalentEquipment):
    """The class represents equivalent branches.
    """
    # Negative sequence series resistance from terminal sequence  1 to terminal
    # sequence 2. Used for short circuit data exchange according to IEC 60909
    # EquivalentBranch is a result of network reduction prior to the data exchange 
    negativeR12: Resistance  = None
 
    # Negative sequence series resistance from terminal sequence 2 to terminal
    # sequence 1. Used for short circuit data exchange according to IEC 60909
    # EquivalentBranch is a result of network reduction prior to the data exchange
    negativeR21: Resistance  = None
 
    # Negative sequence series reactance from terminal sequence  1 to terminal
    # sequence 2. Used for short circuit data exchange according to IEC 60909
    # Usage : EquivalentBranch is a result of network reduction prior to the data
    # exchange
    negativeX12: Reactance  = None
 
    # Negative sequence series reactance from terminal sequence 2 to terminal
    # sequence 1. Used for short circuit data exchange according to IEC 60909.
    # Usage: EquivalentBranch is a result of network reduction prior to the data
    # exchange
    negativeX21: Reactance  = None
 
    # Positive sequence series resistance from terminal sequence  1 to terminal
    # sequence 2 . Used for short circuit data exchange according to IEC 60909.
    # EquivalentBranch is a result of network reduction prior to the data exchange. 
    positiveR12: Resistance  = None
 
    # Positive sequence series resistance from terminal sequence 2 to terminal
    # sequence 1. Used for short circuit data exchange according to IEC 60909
    # EquivalentBranch is a result of network reduction prior to the data exchange
    positiveR21: Resistance  = None
 
    # Positive sequence series reactance from terminal sequence  1 to terminal
    # sequence 2. Used for short circuit data exchange according to IEC 60909
    # Usage : EquivalentBranch is a result of network reduction prior to the data
    # exchange
    positiveX12: Reactance  = None
 
    # Positive sequence series reactance from terminal sequence 2 to terminal
    # sequence 1. Used for short circuit data exchange according to IEC 60909
    # Usage : EquivalentBranch is a result of network reduction prior to the data
    # exchange
    positiveX21: Reactance  = None
 
    # Positive sequence series resistance of the reduced branch.
    r: Resistance  = None
 
    # Resistance from terminal sequence 2 to terminal sequence 1 .Used for steady
    # state power flow. This attribute is optional and represent unbalanced network
    # such as off-nominal phase shifter. If only EquivalentBranch.r is given, then
    # EquivalentBranch.r21 is assumed equal to EquivalentBranch.r.
    # Usage rule : EquivalentBranch is a result of network reduction prior to the
    # data exchange.
    r21: Resistance  = None
 
    # Positive sequence series reactance of the reduced branch.
    x: Reactance  = None
 
    # Reactance from terminal sequence 2 to terminal sequence 1 .Used for steady
    # state power flow. This attribute is optional and represent unbalanced network
    # such as off-nominal phase shifter. If only EquivalentBranch.x is given, then
    # EquivalentBranch.x21 is assumed equal to EquivalentBranch.x.
    # Usage rule : EquivalentBranch is a result of network reduction prior to the
    # data exchange.
    x21: Reactance  = None
 
    # Zero sequence series resistance from terminal sequence  1 to terminal sequence
    # 2. Used for short circuit data exchange according to IEC 60909
    # EquivalentBranch is a result of network reduction prior to the data exchange
    zeroR12: Resistance  = None
 
    # Zero sequence series resistance from terminal sequence  2 to terminal sequence
    # 1. Used for short circuit data exchange according to IEC 60909
    # Usage : EquivalentBranch is a result of network reduction prior to the data
    # exchange
    zeroR21: Resistance  = None
 
    # Zero sequence series reactance from terminal sequence  1 to terminal sequence 2.
    # Used for short circuit data exchange according to IEC 60909
    # Usage : EquivalentBranch is a result of network reduction prior to the data
    # exchange
    zeroX12: Reactance  = None
 
    # Zero sequence series reactance from terminal sequence 2 to terminal sequence 1.
    # Used for short circuit data exchange according to IEC 60909
    # Usage : EquivalentBranch is a result of network reduction prior to the data
    # exchange
    zeroX21: Reactance  = None
     