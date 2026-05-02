import math
from models.spatial_object import SpatialObject


class Parcel(SpatialObject):
    def __init__(self, parcel_id, geometry, area, zone):
        super().__init__(geometry)
        self.parcel_id = parcel_id
        self.area = area
        self.zone = zone
        self.buildings = []
        self.adjacent_roads = []

    def compute_area(self):
        meters_per_degree_lat: float = 111320.0
        meters_per_degree_lon: float = 111320.0 * math.cos(math.radians(self.geometry.centroid.y))
        return self.area * meters_per_degree_lat * meters_per_degree_lon

    def add_building(self, building):
        if building not in self.buildings:
            self.buildings.append(building)

    def add_adjacent_road(self, road):
        if road not in self.adjacent_roads:
            self.adjacent_roads.append(road)

    def describe(self):
        return (
            f"Parcel {self.parcel_id}: zone={self.zone}, "
            f"area={self.area}, buildings={len(self.buildings)}, "
            f"adjacent_roads={len(self.adjacent_roads)}"
        )