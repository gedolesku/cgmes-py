from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.String import String     
from ENTSOE.CommonGridModelExchangeStandard.GeographicalLocationProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class CoordinateSystem(IdentifiedObject):
    """Coordinate reference system.
    """
    # A Uniform Resource Name (URN) for the coordinate reference system (crs) used to
    # define 'Location.PositionPoints'.
    # An example would be the European Petroleum Survey Group (EPSG) code for a
    # coordinate reference system, defined in URN under the Open Geospatial
    # Consortium (OGC) namespace as: urn:ogc:def:uom:EPSG::XXXX, where XXXX is an
    # EPSG code (a full list of codes can be found at the EPSG Registry web site http:
    # //www.epsg-registry.org/). To define the coordinate system as being WGS84
    # (latitude, longitude) using an EPSG OGC, this attribute would be urn:ogc:def:
    # uom:EPSG::4236.
    # A profile should limit this code to a set of allowed URNs agreed to by all
    # sending and receiving parties.
    crsUrn_: str  = None
     