"""
This is file which have library class
"""


from .building import Building

# pylint: disable=too-many-arguments
# pylint: disable=relative-beyond-top-level
class Library(Building):
    """
    Class library that have number of halls, number of books which are held there and address.
    """
    money_equivalent = 500

    def __init__(self, number_of_halls=0, number_of_books=0, address="Nowhere",
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
        return f"Number of halls = {self.number_of_halls}," + \
            f"number of books = {self.number_of_books}," + \
            f"address = {self.address}," + \
            f"is residential = {self.is_residential}," + \
            f"year of building = {self.year_of_building}"

    def __repr__(self):
        """
        This is representation method which return string with mame of class, fields and values
        :return:
        string
        """
        return f"Library(Number of halls = {self.number_of_halls}," + \
            f"number of books = {self.number_of_books}," + \
            f"address = {self.address}," + \
            f"is residential = {self.is_residential}," + \
            f"year of building = {self.year_of_building}"

    def calculate_construction_price(self):
        """
        calculates construction price of library
        by multiplying number of books and money equivalent and dividing them by number of halls
        :return:
        float
            returns amount of money to build this library
        """
        return self.number_of_books / self.number_of_halls * self.money_equivalent
