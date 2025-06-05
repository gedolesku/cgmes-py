from __future__ import annotations

from time import perf_counter

from generated.EuropeanStandards.CommonGridModelExchangeStandard.TopologyProfile.Topology.TopologicalNode import \
    TopologicalNode
from runtime.base import parse_file

XML = "cgmes-models/v24/SmallGrid/node-breaker/SmallGridTestConfiguration_BC_TP_v3.0.0.xml"


def run() -> float:
    start = perf_counter()
    nodes = list(parse_file(XML).iter(TopologicalNode))
    dur = perf_counter() - start
    rate = len(nodes) / dur
    print(f"{len(nodes)} nodes in {dur:.3f}s -> {rate:.0f} obj/s")
    return rate


if __name__ == "__main__":
    rate = run()
    assert rate >= 500_000, f"performance below target: {rate:.0f}"
