from pathlib import Path
import shutil
import importlib
import subprocess
import sys
import os
import pathlib

import pytest

from cgmes.runtime import parse_dataset, export_dataset

DATA_DIR = Path("cgmes-models/v24/SmallGrid/node-breaker")


def setup_module(module):
    shutil.rmtree("generated", ignore_errors=True)
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "cgmes_generator",
            "--rebuild",
        ],
        env=env,
        cwd=pathlib.Path(__file__).parents[1],
    )
    importlib.invalidate_caches()


@pytest.mark.parametrize("xml", sorted(DATA_DIR.glob("*.xml")))
def test_roundtrip_all_profiles(xml):
    objs = parse_dataset(xml)
    assert objs, f"no objects parsed from {xml.name}"

    out = Path("export/roundtrip")
    out.mkdir(parents=True, exist_ok=True)
    export_dataset(objs, out)

    for prof in {cls.__module__.split(".")[-2] for cls in objs}:
        f = out / f"{prof}.xml"
        assert f.exists() and f.stat().st_size > 100, f"{f} missing/empty"
