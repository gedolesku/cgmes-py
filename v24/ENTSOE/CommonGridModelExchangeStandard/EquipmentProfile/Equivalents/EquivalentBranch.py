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
    negativeR12_: Resistance  = None
 
    # Negative sequence series resistance from terminal sequence 2 to terminal
    # sequence 1. Used for short circuit data exchange according to IEC 60909
    # EquivalentBranch is a result of network reduction prior to the data exchange
    negativeR21_: Resistance  = None
 
    # Negative sequence series reactance from terminal sequence  1 to terminal
    # sequence 2. Used for short circuit data exchange according to IEC 60909
    # Usage : EquivalentBranch is a result of network reduction prior to the data
    # exchange
    negativeX12_: Reactance  = None
 
    # Negative sequence series reactance from terminal sequence 2 to terminal
    # sequence 1. Used for short circuit data exchange according to IEC 60909.
    # Usage: EquivalentBranch is a result of network reduction prior to the data
    # exchange
    negativeX21_: Reactance  = None
 
    # Positive sequence series resistance from terminal sequence  1 to terminal
    # sequence 2 . Used for short circuit data exchange according to IEC 60909.
    # EquivalentBranch is a result of network reduction prior to the data exchange. 
    positiveR12_: Resistance  = None
 
    # Positive sequence series resistance from terminal sequence 2 to terminal
    # sequence 1. Used for short circuit data exchange according to IEC 60909
    # EquivalentBranch is a result of network reduction prior to the data exchange
    positiveR21_: Resistance  = None
 
    # Positive sequence series reactance from terminal sequence  1 to terminal
    # sequence 2. Used for short circuit data exchange according to IEC 60909
    # Usage : EquivalentBranch is a result of network reduction prior to the data
    # exchange
    positiveX12_: Reactance  = None
 
    # Positive sequence series reactance from terminal sequence 2 to terminal
    # sequence 1. Used for short circuit data exchange according to IEC 60909
    # Usage : EquivalentBranch is a result of network reduction prior to the data
    # exchange
    positiveX21_: Reactance  = None
 
    # Positive sequence series resistance of the reduced branch.
    r_: Resistance  = None
 
    # Resistance from terminal sequence 2 to terminal sequence 1 .Used for steady
    # state power flow. This attribute is optional and represent unbalanced network
    # such as off-nominal phase shifter. If only EquivalentBranch.r is given, then
    # EquivalentBranch.r21 is assumed equal to EquivalentBranch.r.
    # Usage rule : EquivalentBranch is a result of network reduction prior to the
    # data exchange.
    r21_: Resistance  = None
 
    # Positive sequence series reactance of the reduced branch.
    x_: Reactance  = None
 
    # Reactance from terminal sequence 2 to terminal sequence 1 .Used for steady
    # state power flow. This attribute is optional and represent unbalanced network
    # such as off-nominal phase shifter. If only EquivalentBranch.x is given, then
    # EquivalentBranch.x21 is assumed equal to EquivalentBranch.x.
    # Usage rule : EquivalentBranch is a result of network reduction prior to the
    # data exchange.
    x21_: Reactance  = None
 
    # Zero sequence series resistance from terminal sequence  1 to terminal sequence
    # 2. Used for short circuit data exchange according to IEC 60909
    # EquivalentBranch is a result of network reduction prior to the data exchange
    zeroR12_: Resistance  = None
 
    # Zero sequence series resistance from terminal sequence  2 to terminal sequence
    # 1. Used for short circuit data exchange according to IEC 60909
    # Usage : EquivalentBranch is a result of network reduction prior to the data
    # exchange
    zeroR21_: Resistance  = None
 
    # Zero sequence series reactance from terminal sequence  1 to terminal sequence 2.
    # Used for short circuit data exchange according to IEC 60909
    # Usage : EquivalentBranch is a result of network reduction prior to the data
    # exchange
    zeroX12_: Reactance  = None
 
    # Zero sequence series reactance from terminal sequence 2 to terminal sequence 1.
    # Used for short circuit data exchange according to IEC 60909
    # Usage : EquivalentBranch is a result of network reduction prior to the data
    # exchange
    zeroX21_: Reactance  = None
     