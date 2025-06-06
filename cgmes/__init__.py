"""cgmes package exposing runtime helpers."""

import sys
from importlib import import_module

runtime = import_module("runtime")
sys.modules[__name__ + ".runtime"] = runtime

from runtime import parse_file, parse_dataset, to_element, parse_dataclass  # noqa: F401

__all__ = ["parse_file", "parse_dataset", "to_element", "parse_dataclass", "runtime"]
