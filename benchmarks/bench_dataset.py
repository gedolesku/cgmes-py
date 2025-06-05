"""Dataset parsing benchmark for CGMES profiles."""

from __future__ import annotations

import importlib
import os
import time
from pathlib import Path

from generate_cgmes_project import generate_dataclasses
from runtime.base import parse_file


DEFAULT_DIR = Path("cgmes-models/v24/SmallGrid/node-breaker")
XMI_PATH = "cgmes-models/v24/ENTSOE_CGMES_v2.4.15_7Aug2014.xml"


def bench() -> float:
    """Return objects/s for parsing EQ + SSH files."""
    bench_dir = Path(os.environ.get("CGMES_BENCH_DIR", DEFAULT_DIR))
    eq = bench_dir / "SmallGridTestConfiguration_BC_EQ_v3.0.0.xml"
    tp = bench_dir / "SmallGridTestConfiguration_BC_TP_v3.0.0.xml"
    sv = bench_dir / "SmallGridTestConfiguration_BC_SV_v3.0.0.xml"
    ssh = bench_dir / "SmallGridTestConfiguration_BC_SSH_v3.0.0.xml"
    for f in (eq, tp, sv, ssh):
        if not f.exists():
            raise FileNotFoundError(f)

    if not Path("generated").exists():
        generate_dataclasses(XMI_PATH, "generated")

    tn_mod = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.TopologyProfile.Topology.TopologicalNode"
    )
    sv_mod = importlib.import_module(
        "generated.EuropeanStandards.CommonGridModelExchangeStandard.StateVariablesProfile.StateVariables.SvVoltage"
    )
    TopologicalNode = tn_mod.TopologicalNode
    SvVoltage = sv_mod.SvVoltage

    count = 0
    start = time.perf_counter()
    for file in (eq, tp):
        for _ in parse_file(str(file), TopologicalNode):
            count += 1
    for file in (sv, ssh):
        for _ in parse_file(str(file), SvVoltage):
            count += 1
    elapsed = time.perf_counter() - start
    return count / elapsed


if __name__ == "__main__":
    thr = bench()
    print(f"{thr:.2f} objects/s")
