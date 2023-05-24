"""
This is file which have building class
"""
from abc import ABC, abstractmethod


# pylint: disable=line-too-long
# pylint: disable=relative-beyond-top-level
class Building(ABC):
    """
    This is abstract building class
    """
    def __init__(self, year_of_building=0, is_residential=False):
        self.year_of_building = year_of_building
        self.is_residential = is_residential

    @abstractmethod
    def calculate_construction_price(self):
        """
        This is abstract method which have implementation in children class
        """
        # pass

    def __str__(self):
        """
        This is method which return string with fields and values of the class
        :return:
        string
        """
        return f"Building(year_of_building={self.year_of_building}, " + \
            f"is_residential={self.is_residential})"

    def __repr__(self):
        """
        This is representation method which return string with mame of class, fields and values
        :return:
        string
        """
        return f"Building(year_of_building={self.year_of_building}, " + \
            f"is_residential={self.is_residential})"
