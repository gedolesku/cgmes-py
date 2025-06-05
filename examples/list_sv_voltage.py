"""Print SvVoltage magnitudes from the sample model."""

from cgmes.runtime import parse_file
from cgmes.generated.statevariables.svvoltage import SvVoltage

path = "cgmes-models/v24/SmallGrid/node-breaker/SmallGridTestConfiguration_BC_SV_v3.0.0.xml"

for sv in parse_file(path, SvVoltage):
    print(sv.v)
