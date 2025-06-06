"""cgmes package exposing runtime helpers."""

from importlib import import_module as _imp
import sys

try:  # optional dependency
    import pkg_resources
except ModuleNotFoundError:  # pragma: no cover - fallback when setuptools absent
    pkg_resources = None
else:  # pragma: no cover - declare namespace if available
    pkg_resources.declare_namespace(__name__)

_runtime = _imp("runtime")
sys.modules[__name__ + ".runtime"] = _runtime

from runtime.base import (
    parse_dataclass,
    parse_file as _parse_file,
    parse_dataset,
    to_element,
)

parse_file = _parse_file

__all__ = ["parse_file", "parse_dataset", "to_element", "parse_dataclass"]
