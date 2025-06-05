from enum import Enum

class GeneratorControlSource(Enum):
    unavailable = 'unavailable'
    offAGC = 'offAGC'
    onAGC = 'onAGC'
    plantControl = 'plantControl'
