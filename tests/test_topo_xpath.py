from generated.EuropeanStandards.CommonGridModelExchangeStandard.TopologyProfile.Topology.TopologicalNode import TopologicalNode
from dataclasses import fields
from generated.EuropeanStandards.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

def _meta(name):
    return next(f for f in fields(TopologicalNode) if f.name == name).metadata


def test_xpath_metadata():
    assert _meta("BaseVoltage_id")["xpath"].endswith("/@rdf:resource")
    assert _meta("BaseVoltage_id")["required"] is True
    assert "pattern" in _meta("BaseVoltage_id")
    assert "xpath" not in _meta("BaseVoltage_ref")


def test_inheritance():
    assert issubclass(TopologicalNode, IdentifiedObject)
