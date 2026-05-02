from models.spatial_object import SpatialObject


class Building(SpatialObject):
    def __init__(self, building_id, geometry, height, usage, parcel=None):
        super().__init__(geometry)
        self.building_id = building_id
        self.height = height
        self.usage = usage
        self.parcel = parcel
        self.households = []

        if self.parcel is not None:
            self.parcel.add_building(self)

    def get_height(self):
        return self.height

    def assign_parcel(self, parcel):
        self.parcel = parcel
        parcel.add_building(self)

    def add_household(self, household):
        if household not in self.households:
            self.households.append(household)

    def total_household_income(self):
        return sum(h.income for h in self.households)

    def describe(self):
        parcel_text = self.parcel.parcel_id if self.parcel else "None"
        return (
            f"Building {self.building_id}: usage={self.usage}, "
            f"height={self.height}, parcel={parcel_text}, "
            f"households={len(self.households)}"
        )