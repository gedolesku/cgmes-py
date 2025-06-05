from dataclasses import dataclass
import pytest
from runtime.linker import resolve


@dataclass
class Bus:
    mRID: str


@dataclass
class Load:
    mRID: str
    Bus_id: str | None = None
    Bus_ref: Bus | None = None


def test_resolve_basic():
    bus = Bus(mRID="B1")
    load = Load(mRID="L1", Bus_id="#B1")
    resolve([bus, load])
    assert load.Bus_ref is bus


def test_resolve_missing():
    load = Load(mRID="L1", Bus_id="#B2")
    with pytest.raises(KeyError):
        resolve([load])
