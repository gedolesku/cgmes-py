from pathlib import Path
from tempfile import TemporaryDirectory
import importlib
import shutil
import subprocess
import sys
import os
import pathlib

from cgmes.runtime import parse_dataset, export_dataset, parse_file
import runtime.base as rt_base

DATA = Path("cgmes-models/v24/SmallGrid/node-breaker")
EQ_FILE = DATA / "SmallGridTestConfiguration_BC_EQ_v3.0.0.xml"
TP_FILE = DATA / "SmallGridTestConfiguration_BC_TP_v3.0.0.xml"
SSH_FILE = DATA / "SmallGridTestConfiguration_BC_SSH_v3.0.0.xml"
SV_FILE = DATA / "SmallGridTestConfiguration_BC_SV_v3.0.0.xml"
GL_FILE = DATA / "SmallGridTestConfiguration_BC_GL_v3.0.0.xml"
DL_FILE = DATA / "SmallGridTestConfiguration_BC_DL_v3.0.0.xml"

PowerTransformer = PowerTransformerEnd = None
TopologicalNode_TP = SynchronousMachine_SSH = SvVoltage = Location = Diagram = None


def setup_module(module):
    shutil.rmtree("generated", ignore_errors=True)
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    subprocess.check_call(
        [sys.executable, "-m", "cgmes_generator", "--rebuild"],
        env=env,
        cwd=pathlib.Path(__file__).parents[1],
    )
    importlib.invalidate_caches()
    module.PowerTransformer = importlib.import_module(
        "generated.equipment.PowerTransformer"
    ).PowerTransformer
    module.PowerTransformerEnd = importlib.import_module(
        "generated.equipment.PowerTransformerEnd"
    ).PowerTransformerEnd
    module.TopologicalNode_TP = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.TopologyProfile.Topology.TopologicalNode"
    ).TopologicalNode
    module.SynchronousMachine_SSH = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Wires.SynchronousMachine"
    ).SynchronousMachine
    module.SvVoltage = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.StateVariablesProfile.StateVariables.SvVoltage"
    ).SvVoltage
    module.Location = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.GeographicalLocationProfile.Common.Location"
    ).Location
    module.Diagram = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.DiagramLayoutProfile.DiagramLayout.Diagram"
    ).Diagram
    module._old_ns = rt_base.NS["cim"]
    rt_base.NS["cim"] = "http://iec.ch/TC57/2013/CIM-schema-cim16#"
    for cls in (
        module.PowerTransformer,
        module.PowerTransformerEnd,
        module.TopologicalNode_TP,
        module.SynchronousMachine_SSH,
        module.SvVoltage,
        module.Location,
        module.Diagram,
    ):
        rt_base._SPEC_CACHE.pop(cls, None)


def teardown_module(module):
    rt_base.NS["cim"] = module._old_ns
    for cls in (
        module.PowerTransformer,
        module.PowerTransformerEnd,
        module.TopologicalNode_TP,
        module.SynchronousMachine_SSH,
        module.SvVoltage,
        module.Location,
        module.Diagram,
    ):
        rt_base._SPEC_CACHE.pop(cls, None)


def test_full_bundle_roundtrip():
    objs = {}
    for file, classes in [
        (EQ_FILE, [PowerTransformer, PowerTransformerEnd]),
        (TP_FILE, [TopologicalNode_TP]),
        (SSH_FILE, [SynchronousMachine_SSH]),
        (SV_FILE, [SvVoltage]),
        (GL_FILE, [Location]),
        (DL_FILE, [Diagram]),
    ]:
        data = parse_dataset(str(file), classes)
        for cls, seq in data.items():
            objs.setdefault(cls, []).extend(seq)

    with TemporaryDirectory() as tmp:
        export_dataset(objs, tmp)
        for xml in Path(tmp).glob("*.xml"):
            cls = next(iter(objs))
            list(parse_file(xml, cls))
