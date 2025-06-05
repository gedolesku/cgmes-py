from __future__ import annotations

from dataclasses import fields
from typing import Any, Iterable, Iterator, Type, TypeVar

from lxml import etree

NS = {
    "cim": "http://iec.ch/TC57/2013/CIM-schema-cim16#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
}

T = TypeVar("T")


def _ensure(elem: etree._Element, path: str) -> etree._Element:
    cur = elem
    for part in path.split("/"):
        tag = _q(part)
        child = cur.find(tag, NS)
        if child is None:
            child = etree.SubElement(cur, tag, nsmap=elem.nsmap)
        cur = child
    return cur


def _q(tag: str) -> str:
    if ":" in tag:
        prefix, name = tag.split(":", 1)
        uri = NS.get(prefix)
        if uri:
            return f"{{{uri}}}{name}"
    return tag


def parse_dataclass(cls: Type[T], elem: etree._Element, *, strict: bool = False) -> T:
    values: dict[str, Any] = {}
    for f in fields(cls):
        xp = f.metadata.get("xpath")
        if not xp:
            continue
        val = None
        if xp.startswith("@"):  # attribute on current element
            val = elem.get(xp[1:])
        elif "/@" in xp:
            path, attr = xp.split("/@")
            child = elem.find(_q(path), NS)
            if child is not None:
                if ":" in attr:
                    prefix, name = attr.split(":", 1)
                    ns = NS.get(prefix)
                    key = f"{{{ns}}}{name}" if ns else attr
                else:
                    key = attr
                val = child.get(key)
        else:
            child = elem.find(_q(xp), NS)
            if child is not None:
                val = child.text
        values[f.name] = val
    obj = cls()
    for k, v in values.items():
        setattr(obj, k, v)
    if strict:
        from .validation import validate_required

        validate_required(obj)
    return obj


class _Model:
    def __init__(self, tree: etree._ElementTree):
        self.tree = tree

    def iter(self, cls: Type[T]) -> Iterator[T]:
        tag = f"cim:{cls.__name__}"
        for elem in self.tree.iterfind(f".//{tag}", NS):
            yield parse_dataclass(cls, elem)

    def first(self, cls: Type[T]) -> T | None:
        tag = f"cim:{cls.__name__}"
        elem = self.tree.find(f".//{tag}", NS)
        return parse_dataclass(cls, elem) if elem is not None else None


def parse_file(path: str) -> _Model:
    tree = etree.parse(path)
    return _Model(tree)


def to_element(obj: Any, tag: str | None = None) -> etree._Element:
    cls = obj.__class__
    tag = tag or f"cim:{cls.__name__}"
    elem = etree.Element(tag, nsmap=NS)
    for f in fields(cls):
        xp = f.metadata.get("xpath")
        if not xp:
            continue
        val = getattr(obj, f.name)
        if val is None:
            continue
        if xp.startswith("@"):
            elem.set(xp[1:], str(val))
        elif "/@" in xp:
            path, attr = xp.split("/@")
            child = _ensure(elem, path)
            if ":" in attr:
                prefix, name = attr.split(":", 1)
                ns = NS.get(prefix)
                key = f"{{{ns}}}{name}" if ns else attr
            else:
                key = attr
            child.set(key, str(val))
        else:
            child = _ensure(elem, xp)
            child.text = str(val)
    return elem
