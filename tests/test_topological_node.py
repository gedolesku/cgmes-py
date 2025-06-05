from dataclasses import dataclass, field
from lxml import etree
from runtime.base import parse_dataclass, to_element, parse_file
from generated.EuropeanStandards.CommonGridModelExchangeStandard.TopologyProfile.Topology.TopologicalNode import TopologicalNode

data_xml = (
      """
      <cim:TopologicalNode rdf:ID="_0471bd2a-c766-11e1-8775-005056c00008">
    <cim:IdentifiedObject.name>HickryCk</cim:IdentifiedObject.name>
    <cim:TopologicalNode.ConnectivityNodeContainer rdf:resource="#_047eb579-c766-11e1-8775-005056c00008" />
    <cim:TopologicalNode.BaseVoltage rdf:resource="#_c63f79cc-7953-4ab6-9fa6-f8c729bf895b" />
  </cim:TopologicalNode>
  """
)



def test_roundtrip(tmp_path):
    elem = etree.fromstring(data_xml)
    obj = parse_dataclass(elem, TopologicalNode)
    out_elem = to_element(obj)
    
    print(f"e1={etree.tostring(out_elem)}\ne2={etree.tostring(elem)}")
    assert etree.tostring(out_elem) == etree.tostring(elem)

    # streaming helper
    file = tmp_path / "tn.xml"
    file.write_text(f"<root>{data_xml}</root>")
    objs = list(parse_file(str(file), TopologicalNode))
    assert len(objs) == 1
    assert objs[0].name == "HickryCk"
    assert objs[0].BaseVoltage_id == "#_c63f79cc-7953-4ab6-9fa6-f8c729bf895b"
