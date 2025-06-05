from enum import Enum

class RemoteSignalKind(Enum):
    remoteBusVoltageFrequency = 'remoteBusVoltageFrequency'
    remoteBusVoltageFrequencyDeviation = 'remoteBusVoltageFrequencyDeviation'
    remoteBusFrequency = 'remoteBusFrequency'
    remoteBusFrequencyDeviation = 'remoteBusFrequencyDeviation'
    remoteBusVoltageAmplitude = 'remoteBusVoltageAmplitude'
    remoteBusVoltage = 'remoteBusVoltage'
    remoteBranchCurrentAmplitude = 'remoteBranchCurrentAmplitude'
    remoteBusVoltageAmplitudeDerivative = 'remoteBusVoltageAmplitudeDerivative'
    remotePuBusVoltageDerivative = 'remotePuBusVoltageDerivative'
