"""Runtime helpers source code."""

BASE_SRC = """from __future__ import annotations

from dataclasses import dataclass, field, fields
from typing import List, Optional

from rdflib import Graph, Literal, Namespace, RDF, URIRef

CIM = Namespace('http://iec.ch/TC57/2013/CIM-schema-cim#')

@dataclass
class CIMObject:
    rdf_id: str

    _cim_type: str = 'CIMObject'

    def to_rdf(self, g: Graph) -> URIRef:
        subj = URIRef(f'#{self.rdf_id}')
        g.add((subj, RDF.type, CIM[self._cim_type]))
        g.add((subj, CIM['IdentifiedObject.mRID'], Literal(self.rdf_id)))
        for f in fields(self):
            if f.name == 'rdf_id':
                continue
            pred = CIM[f.metadata.get('cim', f.name).split('.')[-1]]
            val = getattr(self, f.name)
            if val is None:
                continue
            if isinstance(val, list):
                for v in val:
                    _add(subj, pred, v, g)
            else:
                _add(subj, pred, val, g)
        return subj


def _add(s: URIRef, p: URIRef, v, g: Graph):
    if hasattr(v, 'rdf_id'):
        g.add((s, p, URIRef(f'#{v.rdf_id}')))
    else:
        g.add((s, p, Literal(v)))
"""
