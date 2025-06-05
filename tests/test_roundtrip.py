import shutil

from lxml import etree

from generate_cgmes_project import generate_dataclasses
from runtime.base import NS, parse_dataclass, parse_file, to_element

XML = "cgmes-models/v24/SmallGrid/node-breaker/SmallGridTestConfiguration_BC_TP_v3.0.0.xml"
XMI = "cgmes-models/v24/ENTSOE_CGMES_v2.4.15_7Aug2014.xml"


def setup_module(module):
    shutil.rmtree("generated", ignore_errors=True)
    generate_dataclasses(XMI, "generated")


def test_write_single():
    from generated.EuropeanStandards.CommonGridModelExchangeStandard.TopologyProfile.Topology.TopologicalNode import \
        TopologicalNode

    tree = etree.parse(XML)
    elem = tree.find(".//cim:TopologicalNode", namespaces=NS)
    assert elem is not None
    obj = parse_dataclass(TopologicalNode, elem)
    new_elem = to_element(obj, elem.tag)
    new = etree.tostring(new_elem, method="c14n")
    orig = etree.tostring(elem, method="c14n")
    assert new == orig
