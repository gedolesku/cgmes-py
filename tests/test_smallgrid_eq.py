from pathlib import Path
import importlib
import shutil
import subprocess
import sys
import os
import pathlib

from cgmes.runtime import parse_dataset
import runtime.base as rt_base

PowerTransformer = None
PowerTransformerEnd = None

DATA_DIR = Path("cgmes-models/v24/SmallGrid/node-breaker")
XML_FILE = DATA_DIR / "SmallGridTestConfiguration_BC_EQ_v3.0.0.xml"


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
    global PowerTransformer, PowerTransformerEnd
    PowerTransformer = importlib.import_module(
        "generated.equipment.PowerTransformer"
    ).PowerTransformer
    PowerTransformerEnd = importlib.import_module(
        "generated.equipment.PowerTransformerEnd"
    ).PowerTransformerEnd
    module._old_ns = rt_base.NS["cim"]
    rt_base.NS["cim"] = "http://iec.ch/TC57/2013/CIM-schema-cim16#"
    rt_base._SPEC_CACHE.pop(PowerTransformer, None)
    rt_base._SPEC_CACHE.pop(PowerTransformerEnd, None)


def teardown_module(module):
    rt_base.NS["cim"] = module._old_ns
    rt_base._SPEC_CACHE.pop(PowerTransformer, None)
    rt_base._SPEC_CACHE.pop(PowerTransformerEnd, None)


def test_parse_power_transformers():
    data = parse_dataset(str(XML_FILE), [PowerTransformer, PowerTransformerEnd])
    assert len(data[PowerTransformer]) == 10
    assert all(pe.PowerTransformer_id for pe in data[PowerTransformerEnd])
