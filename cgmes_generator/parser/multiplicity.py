"""Helpers for interpreting UML multiplicities."""

from __future__ import annotations

from typing import Tuple

from lxml import etree


def mult_from_elem(elem: etree._Element) -> Tuple[str, str]:
    """Return multiplicity (lower, upper) from UML element."""
    lower = elem.get("lower") or elem.get("lowerValue") or "1"
    upper = elem.get("upper") or elem.get("upperValue") or "1"
    if lower == "":
        lower = "1"
    if upper == "":
        upper = "1"
    if (lv := elem.find("lowerValue")) is not None:
        lower = lv.get("value") or lower
    if (uv := elem.find("upperValue")) is not None:
        upper = uv.get("value") or upper
    return lower, upper


def ptype(base: str, lower: str, upper: str) -> str:
    """Return Python type based on UML multiplicity."""
    if upper == "*" or (upper.isdigit() and int(upper) > 1):
        return f"list[{base}]"
    if lower == "0":
        return f"Optional[{base}]"
    return base
