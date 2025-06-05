from dataclasses import dataclass, field
from lxml import etree
from runtime.base import parse_dataclass, to_element, parse_file
from generated.EuropeanStandards.CommonGridModelExchangeStandard.TopologyProfile.Topology.TopologicalNode import TopologicalNode

data_xml = (
    '<cim:TopologicalNode xmlns:cim="http://iec.ch/TC57/2013/CIM-schema-cim#" '
    'xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">'
    "<cim:TopologicalNode.name>Node</cim:TopologicalNode.name>"
    '<cim:TopologicalNode.BaseVoltage rdf:resource="#BV1"/>'
    "</cim:TopologicalNode>"
)



def test_roundtrip(tmp_path):
    elem = etree.fromstring(data_xml)
    obj = parse_dataclass(elem, TopologicalNode)
    out_elem = to_element(obj)
    assert etree.tostring(out_elem) == etree.tostring(elem)

    # streaming helper
    file = tmp_path / "tn.xml"
    file.write_text(f"<root>{data_xml}</root>")
    objs = list(parse_file(str(file), TopologicalNode))
    assert len(objs) == 1
    assert objs[0].name == "Node"
    assert objs[0].BaseVoltage_id == "#BV1"
