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
    purposes = {}

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
        return str(f"{self.__dict__}")

    def __repr__(self):
        """
        This is representation method which return string with mame of class, fields and values
        :return:
        string
        """
        return str(f"{self.__class__.__name__}: {self.__dict__}")

    def all_values_with_type(self, type_of_value):
        return {k: v for k, v in self.__dict__.items() if type(v) == type_of_value}
