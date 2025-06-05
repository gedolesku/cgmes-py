from enum import Enum

class DroopSignalFeedbackKind(Enum):
    electricalPower = 'electricalPower'
    none = 'none'
    fuelValveStroke = 'fuelValveStroke'
    governorOutput = 'governorOutput'
