"""
This is file which have zoo class
"""
from Zoo.decorators.decorators import logged
from Zoo.model.building import Building
from Zoo.exceptions.exceptions import ConstructionNotExisting, TooLittleSpace


# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=relative-beyond-top-level
class Zoo(Building):
    """
    Class zoo that have name capacity, area, where it locates and name.
    """
    instance = None
    money_equivalent = 2000
    purposes = {'conservation and species preservation',
                                    'recreation and inspiration',
                                    'research and scientific advancement'}

    def __init__(self, area=1, capacity=1, name="noname", location="nowhere",
                 year_of_building=0, is_residential=False):
        self.area = area
        self.capacity = capacity
        self.name = name
        self.location = location
        super().__init__(year_of_building, is_residential)

    def __str__(self):
        """
        This is method which return string with fields and values of the class
        :return:
        string
        """
        return str(f"{self.__dict__}")

    def __repr__(self):
        """
        This is representation method which return string with mame of class, fields and values
        :return:
        string
        """
        return str(f"{self.__class__.__name__}: {self.__dict__}")

    def __cmp__(self, other):
        return self.area == other.area \
            and self.capacity == other.capacity and \
            self.location == other.location and \
            self.name == other.name and \
            self.is_residential == other.is_residential and \
            self.year_of_building == other.year_of_building

    @staticmethod
    def get_instance():
        """
        Returns the singleton instance of the Zoo class.
        If no instance exists, a new instance is created.
        Returns:
        --------
        Zoo
            The singleton instance of the Zoo class.
        """
        if not Zoo.instance:
            Zoo.instance = Zoo()
        return Zoo.instance

    @logged("file")
    def increase_capacity(self, capacity):
        """
        This method increases capacity and return the new value of it
        :return
        int
            returns new capacity value
        """
        if self.area - 10 < self.capacity:
            raise TooLittleSpace(self.area, self.capacity)
        self.capacity += capacity
        return self.capacity

    def split_area(self):
        """
        This method split area in a half and return the new value of it
        :return
        float
            returns new area value
        """
        self.area /= 2
        return self.area

    def add_new_region(self, area):
        """
        This method increases area of zoo and add a new region to location
        :return
        float
            returns new area value
        """
        self.location += ", New Region"
        self.area += area
        return self.area

    @logged("console")
    def calculate_construction_price(self):
        """calculates construction price of zoo
        by multiplying area and money equivalent and dividing them by capacity
        :return
        int
            returns amount of money to build this zoo
        """
        if not self.capacity:
            raise ConstructionNotExisting
        return int(self.area / self.capacity * self.money_equivalent)
