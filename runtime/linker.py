from __future__ import annotations

"""In-memory reference resolver for CGMES dataclasses."""

from typing import Any, Iterable


def resolve(model_objects: Iterable[Any]) -> None:
    """Resolve ``*_id`` attributes to ``*_ref`` on *model_objects*.

    Objects are indexed by ``mRID`` or ``rdf_ID`` (if present). For every
    attribute ending with ``_id`` a corresponding ``*_ref`` attribute is
    looked up in the index and set to the target object. A :class:`KeyError`
    is raised if the reference target cannot be found.
    """

    objs = list(model_objects)
    index: dict[str, Any] = {}
    for obj in objs:
        obj_id = getattr(obj, "mRID", None)
        if obj_id is None:
            obj_id = getattr(obj, "rdf_ID", None)
        if obj_id is not None:
            index[obj_id] = obj

    for obj in objs:
        for attr in list(vars(obj)):
            if not attr.endswith("_id"):
                continue
            val = getattr(obj, attr)
            if val is None:
                continue
            ref_attr = attr[:-3] + "_ref"
            if not hasattr(obj, ref_attr):
                continue
            target = index.get(val.lstrip("#"))
            if target is None:
                raise KeyError(val)
            setattr(obj, ref_attr, target)
