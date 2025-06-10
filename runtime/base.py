from __future__ import annotations

"""Minimal runtime helpers for CGMES dataclasses."""
from dataclasses import fields
from typing import Any, Dict, Iterator, List, Tuple, Type, TypeVar
from lxml import etree

NS = {
    "cim": "http://iec.ch/TC57/2013/CIM-schema-cim#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
}

T = TypeVar("T")

_SPEC_CACHE: Dict[Type[Any], List[Tuple[str | None, str | None, str]]] = {}
_ALL_CLASSES: List[Type[Any]] | None = None


def _load_all_classes() -> List[Type[Any]]:
    """Return all generated dataclasses lazily."""
    global _ALL_CLASSES
    if _ALL_CLASSES is not None:
        return _ALL_CLASSES
    from importlib import import_module
    import pkgutil
    from dataclasses import is_dataclass

    try:
        import generated
    except ModuleNotFoundError:  # pragma: no cover - generator not run yet
        _ALL_CLASSES = []
        return _ALL_CLASSES

    classes: List[Type[Any]] = []
    for info in pkgutil.walk_packages(generated.__path__, generated.__name__ + "."):
        mod = import_module(info.name)
        for obj in vars(mod).values():
            if isinstance(obj, type) and is_dataclass(obj):
                classes.append(obj)
    _ALL_CLASSES = classes
    return classes


def _spec(cls: Type[Any]) -> List[Tuple[str | None, str | None, str]]:
    """Return cached ``(tag, attr, field)`` mapping for *cls* fields."""

    spec = _SPEC_CACHE.get(cls)
    if spec is not None:
        return spec
    spec_list: List[Tuple[str | None, str | None, str]] = []
    for f in fields(cls):
        xp = f.metadata.get("xpath")
        if not xp:
            continue
        tag: str | None
        attr: str | None = None
        if xp.startswith("@"):
            tag = None
            attr = xp[1:]
        else:
            if xp.endswith("/text()"):
                tag = xp[:-7]
                attr = "text"
            elif "/@" in xp:
                tag, attr = xp.rsplit("/@", 1)
            else:
                tag = xp
            if tag:
                pre, local = tag.split(":", 1)
                tag = f"{{{NS[pre]}}}{local}"
        if attr and attr != "text" and ":" in attr:
            pre, local = attr.split(":", 1)
            attr = f"{{{NS[pre]}}}{local}"
        spec_list.append((tag, attr, f.name))
    _SPEC_CACHE[cls] = spec_list
    return spec_list


def parse_dataclass(elem: etree._Element, cls: Type[T]) -> T:
    """Parse *elem* into an instance of *cls* based on ``xpath`` metadata."""
    child_map = {c.tag: c for c in elem}
    obj = cls.__new__(cls)
    for tag, attr, fname in _spec(cls):
        if tag is None:
            value = elem.get(attr) if attr else None
        else:
            child = child_map.get(tag)
            if child is None:
                value = None
            else:
                if attr is None or attr == "text":
                    value = child.text
                else:
                    value = child.get(attr)
        setattr(obj, fname, value)
    return obj


def to_element(obj: Any) -> etree._Element:
    """Serialize *obj* back into an XML element."""
    cls = type(obj)
    root = etree.Element(f"{{{NS['cim']}}}{cls.__name__}", nsmap=NS)
    for tag, attr, fname in _spec(cls):
        value = getattr(obj, fname)
        if value is None:
            continue
        if tag is None:
            if attr:
                root.set(attr, str(value))
            continue
        child = etree.SubElement(root, tag)
        if attr is None or attr == "text":
            child.text = str(value)
        else:
            child.set(attr, str(value))
    return root


def parse_file(path: str, cls: Type[T]) -> Iterator[T]:
    """Yield ``cls`` objects from *path* using ``iterparse`` streaming."""
    tag = f"{{{NS['cim']}}}{cls.__name__}"
    for _event, elem in etree.iterparse(path, events=("end",), tag=tag):
        yield parse_dataclass(elem, cls)
        elem.clear()


def parse_dataset(
    path: str, classes: List[Type[Any]] | None = None
) -> Dict[Type[Any], List[Any]]:
    """Parse *path* once and collect objects of ``classes``.

    Example
    -------
    >>> data = parse_dataset("model.xml", [TopologicalNode, VoltageLevel])
    >>> len(data[TopologicalNode])
    10
    """
    if classes is None:
        classes = _load_all_classes()
    qname_map = {f"{{{NS['cim']}}}{cls.__name__}": cls for cls in classes}
    result: Dict[Type[Any], List[Any]] = {cls: [] for cls in classes}
    tags = tuple(qname_map)
    for _event, elem in etree.iterparse(path, events=("end",), tag=tags):
        cls = qname_map[elem.tag]
        result[cls].append(parse_dataclass(elem, cls))
        elem.clear()
    from . import validation

    validation.validate(result, strict=True)
    validation.resolve(result)
    return result
