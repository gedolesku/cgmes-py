from generate_cgmes_project import generate_dataclasses
import importlib
import shutil
from typing import get_type_hints


def setup_module(module):
    shutil.rmtree("generated", ignore_errors=True)
    generate_dataclasses(
        "cgmes-models/v24/ENTSOE_CGMES_v2.4.15_7Aug2014.xml", "generated"
    )


def test_svvoltage_topologicalnode_type():
    sv_mod = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.StateVariablesProfile.StateVariables.SvVoltage"
    )
    tn_mod = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.StateVariablesProfile.Topology.TopologicalNode"
    )
    hints = get_type_hints(
        sv_mod.SvVoltage, globalns=sv_mod.__dict__, localns=sv_mod.__dict__
    )
    assert hints["TopologicalNode_ref"] is tn_mod.TopologicalNode
