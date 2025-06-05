from __future__ import annotations

import pytest
from dataclasses import dataclass, field

from runtime.validation import validate


@dataclass(kw_only=True)
class IdentifiedObject:
    mRID: str | None = field(
        default=None,
        metadata={"xpath": "@rdf:ID", "required": True},
    )
    name: str | None = field(
        default=None,
        metadata={"xpath": "cim:IdentifiedObject.name"},
    )


@dataclass(kw_only=True)
class TopologicalNode(IdentifiedObject):
    BaseVoltage_id: str | None = field(
        default=None,
        metadata={
            "xpath": "cim:TopologicalNode.BaseVoltage/@rdf:resource",
            "required": True,
            "pattern": r"^#.+$",
        },
    )
    BaseVoltage_ref: "BaseVoltage" | None = None
    ConnectivityNodeContainer_id: str | None = field(
        default=None,
        metadata={
            "xpath": "cim:TopologicalNode.ConnectivityNodeContainer/@rdf:resource",
            "required": True,
            "pattern": r"^#.+$",
        },
    )
    ConnectivityNodeContainer_ref: "ConnectivityNodeContainer" | None = None
    ReportingGroup_id: str | None = field(
        default=None,
        metadata={
            "xpath": "cim:TopologicalNode.ReportingGroup/@rdf:resource",
            "pattern": r"^#.+$",
        },
    )
    ReportingGroup_ref: "ReportingGroup" | None = None


def _validate(**kwargs):
    node = TopologicalNode(**kwargs)
    validate({TopologicalNode: [node]}, strict=True)


def test_missing_basevoltage():
    with pytest.raises(ValueError, match="BaseVoltage_id is required"):
        _validate(mRID="n1", ConnectivityNodeContainer_id="#c1")


def test_basevoltage_pattern():
    with pytest.raises(ValueError, match="BaseVoltage_id does not match"):
        _validate(mRID="n1", BaseVoltage_id="BV1", ConnectivityNodeContainer_id="#c1")
