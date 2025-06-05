from generate_cgmes_project import generate_dataclasses
import shutil
import importlib
from dataclasses import fields, is_dataclass


def setup_module(module):
    shutil.rmtree("generated", ignore_errors=True)
    generate_dataclasses(
        "cgmes-models/v24/ENTSOE_CGMES_v2.4.15_7Aug2014.xml", "generated"
    )
    global TopologicalNode, IdentifiedObject
    TopologicalNode = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.TopologyProfile.Topology.TopologicalNode"
    ).TopologicalNode
    IdentifiedObject = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject"
    ).IdentifiedObject


def meta(name):
    return next(f for f in fields(TopologicalNode) if f.name == name).metadata


def test_xpath_and_required():
    assert is_dataclass(TopologicalNode)
    assert meta("BaseVoltage_id")["xpath"].endswith("/@rdf:resource")
    assert meta("BaseVoltage_id")["required"] is True
    assert "pattern" in meta("BaseVoltage_id")
    assert "xpath" not in meta("BaseVoltage_ref")


def test_inheritance():
    assert issubclass(TopologicalNode, IdentifiedObject)
