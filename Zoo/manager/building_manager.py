"""
This is file which have building manager class
"""
from decorators.decorators import write_dictionary_of_kwargs, exception_writer


# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=use-a-generator
class BuildingManager:
    """
    This is class Building manager which have list of buildings and can interact with it
    """

    def __init__(self, buildings):
        self.buildings = buildings
        self.index = 1

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index - 1 > len(self.buildings):
            raise StopIteration
        self.index += 1
        building = self.buildings[self.index - 1]
        return building

    @exception_writer
    def __getitem__(self, index):
        """
        Returns the value at the specified index.

        :param index: The index of the value to retrieve.
        :return: The value at the specified index.
        :raises IndexError: If the index is out of range.
        """
        return self.buildings[index]

    def indexing(self):
        """
        This is method which return list of tuples
        with index and building
        :return:
        enumerate
        """
        return enumerate(self.buildings)

    def calculate_construction_price_for_every_building(self):
        """
        this is method which return a list
        of calculating construction price of every
        building in list of buildings
        :return:
        list
        """
        return [building.calculate_construction_price() for building in self.buildings]

    def pairs_of_building_and_construction_price(self):
        """
        This method which makes a pair of
        building and its construction price
        :return:
        zip
        """
        return zip(self.buildings, self.calculate_construction_price_for_every_building())

    @write_dictionary_of_kwargs
    def add_building(self, building, **kwargs):
        """
        this function add building to list of buildings
        :param building:
        :return:
        """
        print(kwargs)
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
        this is function which find buildings
        that are have year of building bigger than year you input
        :return:
        list
        """
        return list(filter(lambda building: building.year_of_building > year_of_building,
                           self.buildings))

    def is_buildings_build_in(self, year):
        """
        This method which check
         if all buildings built in specific year
        :param year:
        :return:
        boolean
        """
        return all([building.year_of_building == year for building in self.buildings])

    def is_any_residential_building(self):
        """
        This method which check
         if any buildings residential
        :return:
        boolean
        """
        return any([building.is_residential for building in self.buildings])

