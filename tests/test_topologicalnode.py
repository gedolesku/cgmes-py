from generate_cgmes_project import generate_dataclasses
import importlib
import shutil


def setup_module(module):
    shutil.rmtree("generated", ignore_errors=True)
    generate_dataclasses("cgmes-models/v24/ENTSOE_CGMES_v2.4.15_7Aug2014.xml", "generated")


def test_topologicalnode_inheritance():
    """Check TopologicalNode inheritance direction between profiles."""
    tp_mod = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.TopologyProfile.Topology.TopologicalNode"
    )
    sv_mod = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.StateVariablesProfile.Topology.TopologicalNode"
    )
    assert issubclass(tp_mod.TopologicalNode, sv_mod.TopologicalNode)
    assert not issubclass(sv_mod.TopologicalNode, tp_mod.TopologicalNode)


def test_topologicalnode_identifiedobject_base():
    """Ensure TopologicalNode derives from IdentifiedObject."""
    tp_mod = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.TopologyProfile.Topology.TopologicalNode"
    )
    io_mod = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject"
    )
    assert issubclass(tp_mod.TopologicalNode, io_mod.IdentifiedObject)
