import importlib
import shutil
from dataclasses import fields

import subprocess


def setup_module(module):
    shutil.rmtree("generated", ignore_errors=True)
    subprocess.check_call(["python", "-m", "cgmes_generator", "--rebuild"])


def test_topologicalnode_metadata():
    tn_mod = importlib.import_module("generated.topology.TopologicalNode")
    base_mod = importlib.import_module("generated.topology.IdentifiedObject")
    cls = tn_mod.TopologicalNode
    base = base_mod.IdentifiedObject
    assert cls.__doc__ == "Auto-generated — DO NOT EDIT BY HAND"
    assert tn_mod.__all__ == ["TopologicalNode"]
    assert issubclass(cls, base)
    meta = {f.name: f.metadata for f in fields(cls)}
    assert meta["BaseVoltage_id"]["xpath"] == "cim:TopologicalNode.BaseVoltage/@rdf:resource"
    assert meta["ConnectivityNodeContainer_id"]["xpath"] == "cim:TopologicalNode.ConnectivityNodeContainer/@rdf:resource"
    assert meta["ConnectivityNodeContainer_id"]["required"] is True
    assert meta["ConnectivityNodeContainer_id"]["pattern"] == "^#.+$"
    assert meta["ReportingGroup_id"]["xpath"] == "cim:TopologicalNode.ReportingGroup/@rdf:resource"
