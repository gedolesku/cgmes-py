"""Benchmark for parse_dataset helper."""

from pathlib import Path
from cgmes.runtime import parse_dataset

from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class IdentifiedObject:
    mRID: str = field(metadata={"xpath": "@rdf:ID"})


@dataclass(kw_only=True)
class Equipment(IdentifiedObject):
    name: Optional[str] = field(
        default=None, metadata={"xpath": "cim:IdentifiedObject.name/text()"}
    )


DATASET = (
    Path(__file__).resolve().parent.parent
    / "cgmes-models"
    / "v24"
    / "SmallGrid"
    / "node-breaker"
    / "SmallGridTestConfiguration_BC_EQ_v3.0.0.xml"
)


def bench_parse_dataset(benchmark):
    benchmark(lambda: parse_dataset(str(DATASET), [Equipment]))
