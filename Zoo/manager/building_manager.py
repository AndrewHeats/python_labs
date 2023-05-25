"""
This is file which have building manager class
"""
from decorators.decorators import write_dictionary_of_kwargs, exception_writer


# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
class BuildingManager:
    """
    This is class Building manager which have list of buildings and can interact with it
    """

    def __init__(self, buildings=[]):
        self.buildings = buildings
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index - 1 > len(self.buildings):
            raise StopIteration
        else:
            building = self.buildings[self.index - 1]
            self.index += 1
            return building

    def __getitem__(self, item):
        return type(item), item

    def indexing(self):
        return enumerate(self.buildings)

    def calculate_construction_price_for_every_building(self):
        return [building.calculate_construction_price() for building in self.buildings]

    def pairs_of_building_and_construction_price(self):
        return zip(self.buildings, self.calculate_construction_price_for_every_building())

    def add_building(self, building):
        """
        this function add building to list of buildings
        :param building:
        :return:
        """
        self.buildings.append(building)

    @write_dictionary_of_kwargs
    def find_residential_buildings(self):
        """
        this is function which find buildings that are residential
        :return:
        list
        """
        return list(filter(lambda building: building.is_residential, self.buildings))

    @write_dictionary_of_kwargs
    def find_buildings_build_after(self, year_of_building=0):
        """
        this is function which find buildings
        that are have year of building bigger than year you input
        :return:
        list
        """
        return list(filter(lambda building: building.year_of_building > year_of_building,
                           self.buildings))

    @write_dictionary_of_kwargs
    def is_buildings_build_in(self, year=0):
        return all([building.year_of_building == year for building in self.buildings])

    @write_dictionary_of_kwargs
    def is_any_residential_building(self):
        return any([building.is_residential for building in self.buildings])

    @exception_writer
    def some_method(self, t):
        return 1 / t
