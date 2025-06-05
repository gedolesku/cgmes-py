from enum import Enum

class InputSignalKind(Enum):
    rotorSpeed = 'rotorSpeed'
    rotorAngularFrequencyDeviation = 'rotorAngularFrequencyDeviation'
    busFrequency = 'busFrequency'
    busFrequencyDeviation = 'busFrequencyDeviation'
    generatorElectricalPower = 'generatorElectricalPower'
    generatorAcceleratingPower = 'generatorAcceleratingPower'
    busVoltage = 'busVoltage'
    busVoltageDerivative = 'busVoltageDerivative'
    branchCurrent = 'branchCurrent'
    fieldCurrent = 'fieldCurrent'
