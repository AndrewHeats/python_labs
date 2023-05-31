"""
This is file which have library class
"""
from Zoo.decorators.decorators import logged
from Zoo.exceptions.exceptions import ConstructionNotExisting
from Zoo.model.building import Building


# pylint: disable=too-many-arguments
# pylint: disable=relative-beyond-top-level
class Library(Building):
    """
    Class library that have number of halls, number of books which are held there and address.
    """
    money_equivalent = 500
    purposes = {'access to technology', 'archiving', 'research and study support'}

    def __init__(self, number_of_halls=1, number_of_books=1, address="Nowhere",
                 year_of_building=0, is_residential=False):
        self.number_of_halls = number_of_halls
        self.number_of_books = number_of_books
        self.address = address
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

    @logged("file")
    def calculate_construction_price(self):
        """
        calculates construction price of library
        by multiplying number of books and money equivalent and dividing them by number of halls
        :return:
        int
            returns amount of money to build this library
        """
        if not self.number_of_halls:
            raise ConstructionNotExisting
        return int(self.number_of_books / self.number_of_halls * self.money_equivalent)
