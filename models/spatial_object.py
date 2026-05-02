from math import sqrt
from shapely.geometry.base import BaseGeometry


class SpatialObject:
    def __init__(self, geometry: BaseGeometry):
        self.geometry = geometry

    def distance_to(self, other):
        return self.geometry.distance(other.geometry)

    def intersects(self, other) -> bool:
        return self.geometry.intersects(other.geometry)