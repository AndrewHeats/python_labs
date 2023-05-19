class BuildingManager:
    def __init__(self, buildings):
        self.buildings = buildings

    def add_building(self, building):
        self.buildings.append(building)

    def find_residential_buildings(self):
        return list(filter(lambda building: building.is_residential, self.buildings))

    def find_buildings_build_after(self, year_of_building):
        return list(filter(lambda building: building.year_of_building > year_of_building, self.buildings))
