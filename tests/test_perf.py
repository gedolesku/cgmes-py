import shutil
from time import perf_counter

from generate_cgmes_project import generate_dataclasses
from runtime.base import parse_file

XML = "cgmes-models/v24/SmallGrid/node-breaker/SmallGridTestConfiguration_BC_TP_v3.0.0.xml"
XMI = "cgmes-models/v24/ENTSOE_CGMES_v2.4.15_7Aug2014.xml"


def setup_module(module):
    shutil.rmtree("generated", ignore_errors=True)
    generate_dataclasses(XMI, "generated")


def test_perf_parse():
    from generated.EuropeanStandards.CommonGridModelExchangeStandard.TopologyProfile.Topology.TopologicalNode import \
        TopologicalNode

    start = perf_counter()
    nodes = list(parse_file(XML).iter(TopologicalNode))
    rate = len(nodes) / (perf_counter() - start)
    assert rate >= 500_000
