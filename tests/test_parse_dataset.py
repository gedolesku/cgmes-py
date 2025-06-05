from dataclasses import dataclass, field
from typing import Optional
from runtime.base import parse_dataset


data_xml = (
    '<root xmlns:cim="http://iec.ch/TC57/2013/CIM-schema-cim#" '
    'xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">'
    '<cim:VoltageLevel rdf:ID="vl1">'
    "<cim:IdentifiedObject.name>VL1</cim:IdentifiedObject.name>"
    "</cim:VoltageLevel>"
    '<cim:TopologicalNode rdf:ID="tn1">'
    "<cim:TopologicalNode.name>Node1</cim:TopologicalNode.name>"
    '<cim:TopologicalNode.ConnectivityNodeContainer rdf:resource="#vl1"/>'
    "</cim:TopologicalNode>"
    "</root>"
)


@dataclass(kw_only=True)
class IdentifiedObject:
    mRID: str = field(metadata={"xpath": "@rdf:ID", "required": True})
    name: Optional[str] = field(
        default=None, metadata={"xpath": "cim:IdentifiedObject.name/text()"}
    )


@dataclass(kw_only=True)
class VoltageLevel(IdentifiedObject):
    pass


@dataclass(kw_only=True)
class TopologicalNode(IdentifiedObject):
    ConnectivityNodeContainer_id: str = field(
        metadata={
            "xpath": "cim:TopologicalNode.ConnectivityNodeContainer/@rdf:resource",
            "required": True,
            "pattern": "^#.+$",
        }
    )
    ConnectivityNodeContainer_ref: VoltageLevel | None = field(default=None)


def test_parse_dataset(tmp_path):
    file = tmp_path / "data.xml"
    file.write_text(data_xml)
    result = parse_dataset(str(file), [TopologicalNode, VoltageLevel])
    assert len(result[TopologicalNode]) == 1
    assert len(result[VoltageLevel]) == 1
    tn = result[TopologicalNode][0]
    vl = result[VoltageLevel][0]
    assert tn.ConnectivityNodeContainer_ref is vl
