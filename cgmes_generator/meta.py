"""Dataclasses describing parsed UML metadata."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class Attribute:
    """Single attribute parsed from the UML model."""

    name: str
    cim_path: str
    type_: str
    multiplicity: str
    is_ref: bool = False
    ref_pkg: Optional[Tuple[str, ...]] = None
    uml_id: Optional[str] = None  # XMI id, for tracking links


@dataclass
class ClassMeta:
    """Metadata collected for a UML class."""

    name: str
    attrs: Dict[str, Attribute]
    parent: Optional[str]
    pkg_parts: Tuple[str, ...]
    doc: Optional[str] = None
    parent_pkg: Optional[Tuple[str, ...]] = None
    uml_id: Optional[str] = None
    links: List["LinkData"] = field(default_factory=list)
    is_abstract: bool = False


@dataclass
class EnumMeta:
    """Metadata for UML enumerations."""

    name: str
    literals: List[str]
    pkg_parts: Tuple[str, ...]
    doc: Optional[str] = None


@dataclass
class LinkData:
    """Minimal info about XMI links for later tooling."""

    uml_id: str
    kind: str
    start: str
    end: str
