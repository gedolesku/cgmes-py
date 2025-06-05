import importlib
import shutil
from dataclasses import fields

import subprocess
import sys


def setup_module(module):
    subprocess.check_call([sys.executable, "-m", "cgmes_generator", "--rebuild"])


def test_topologicalnode_metadata():
    tn_mod = importlib.import_module("generated.EuropeanStandards.CommonGridModelExchangeStandard.TopologyProfile.Topology.TopologicalNode")
    base_mod = importlib.import_module("generated.EuropeanStandards.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject")
    cls = tn_mod.TopologicalNode
    base = base_mod.IdentifiedObject
    assert issubclass(cls, base)
    meta = {f.name: f.metadata for f in fields(cls)}
    assert (
        meta["BaseVoltage_id"]["xpath"]
        == "cim:TopologicalNode.BaseVoltage/@rdf:resource"
    )
    assert (
        meta["ConnectivityNodeContainer_id"]["xpath"]
        == "cim:TopologicalNode.ConnectivityNodeContainer/@rdf:resource"
    )
    assert meta["ConnectivityNodeContainer_id"]["required"] is True
    assert meta["ConnectivityNodeContainer_id"]["pattern"] == "^#.+$"
    assert (
        meta["ReportingGroup_id"]["xpath"]
        == "cim:TopologicalNode.ReportingGroup/@rdf:resource"
    )


def test_sv_voltage_metadata():
    sv_mod = importlib.import_module("generated.topology.SvVoltage")
    cls = sv_mod.SvVoltage
    meta = {f.name: f.metadata for f in fields(cls)}
    assert (
        meta["TopologicalNode_id"]["xpath"]
        == "cim:SvVoltage.TopologicalNode/@rdf:resource"
    )
    assert meta["TopologicalNode_id"]["required"] is True
    assert meta["TopologicalNode_id"]["pattern"] == "^#.+$"
