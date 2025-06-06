from pathlib import Path
import importlib
import shutil

import cgmes.runtime
from cgmes.runtime import parse_file
from cgmes_generator import generate_dataclasses
import runtime.base as rt_base

TopologicalNode = None

DATA_DIR = Path("cgmes-models/v24/SmallGrid/node-breaker")
XML_FILE = DATA_DIR / "SmallGridTestConfiguration_BC_TP_v3.0.0.xml"


def setup_module(module):
    shutil.rmtree("generated", ignore_errors=True)
    generate_dataclasses(
        "cgmes-models/v24/ENTSOE_CGMES_v2.4.15_7Aug2014.xml",
        "generated",
    )
    global TopologicalNode
    TopologicalNode = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.TopologyProfile.Topology.TopologicalNode"
    ).TopologicalNode
    module._old_ns = rt_base.NS["cim"]
    rt_base.NS["cim"] = "http://iec.ch/TC57/2013/CIM-schema-cim16#"
    rt_base._SPEC_CACHE.pop(TopologicalNode, None)


def teardown_module(module):
    rt_base.NS["cim"] = module._old_ns
    rt_base._SPEC_CACHE.pop(TopologicalNode, None)


def test_parse_topological_nodes():
    nodes = list(parse_file(XML_FILE, TopologicalNode))
    assert len(nodes) == 115
    assert all(n.BaseVoltage_id for n in nodes)


def test_roundtrip_single():
    node = next(parse_file(XML_FILE, TopologicalNode))
    new_elem = cgmes.runtime.to_element(node)
    node2 = parse_file.__wrapped__(new_elem, TopologicalNode)
    assert node2.BaseVoltage_id == node.BaseVoltage_id
