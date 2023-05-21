class BuildingManager:
    """
    This is class Building manager which have list of buildings and can interact with it
    """

    def __init__(self, buildings):
        self.buildings = buildings

    def add_building(self, building):
        """
        this function add building to list of buildings
        :param building:
        :return:
        """
        self.buildings.append(building)

    def find_residential_buildings(self):
        """
        this is function which find buildings that are residential
        :return:
        list
        """
        return list(filter(lambda building: building.is_residential, self.buildings))

    def find_buildings_build_after(self, year_of_building):
        """
        this is function which find buildings that are have year of building bigger than year you input
        :return:
        list
        """
        return list(filter(lambda building: building.year_of_building > year_of_building, self.buildings))
