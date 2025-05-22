from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto

class Currency(Enum):
    """Monetary currencies. Apologies for this list not being exhaustive.
    """
    # US dollar
    USD = auto()
    # European euro
    EUR = auto()
    # Australian dollar
    AUD = auto()
    # Canadian dollar
    CAD = auto()
    # Swiss francs
    CHF = auto()
    # Chinese yuan renminbi
    CNY = auto()
    # Danish crown
    DKK = auto()
    # British pound
    GBP = auto()
    # Japanese yen
    JPY = auto()
    # Norwegian crown
    NOK = auto()
    # Russian ruble
    RUR = auto()
    # Swedish crown
    SEK = auto()
    # India rupees
    INR = auto()
    # Another type of currency.
    other = auto()