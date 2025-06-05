from dataclasses import dataclass, field
import pytest

from runtime.validation import validate


@dataclass
class TopologicalNode:
    mRID: str = field(metadata={"required": True})


@dataclass
class SvVoltage:
    TopologicalNode_id: str | None = field(default=None)


@dataclass
class ConnectivityNode:
    TopologicalNode_id: str | None = field(default=None)


def test_svvoltage_requires_topologicalnode():
    node = TopologicalNode(mRID="#TN1")
    sv = SvVoltage(TopologicalNode_id="#TN1")
    validate(sv, dataset=[node])

    with pytest.raises(ValueError):
        validate(SvVoltage(TopologicalNode_id=None), dataset=[node])

    with pytest.raises(ValueError):
        validate(SvVoltage(TopologicalNode_id="#other"), dataset=[node])


def test_connectivitynode_profile_handling():
    # optional in EQ
    cn_eq = ConnectivityNode()
    validate(cn_eq, profile="EQ")

    # required in SSH
    cn = ConnectivityNode(TopologicalNode_id="#TN1")
    validate(cn, profile="SSH")
    with pytest.raises(ValueError):
        validate(ConnectivityNode(), profile="SSH")
