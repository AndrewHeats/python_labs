"""
This is file which have bank class
"""


from .building import Building
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=relative-beyond-top-level
class Bank(Building):
    """
    Class bank that have number of cashier who working there,
    maximum number of people and open-close hours.
    """
    money_equivalent = 3000

    def __init__(self, number_of_cashier=0, open_close_hours="00:00-00:00", max_number_of_people=0,
                 is_residential=False, year_of_building=0):
        self.number_of_cashier = number_of_cashier
        self.open_close_hours = open_close_hours
        self.max_number_of_people = max_number_of_people
        super().__init__(year_of_building, is_residential)

    def __str__(self):
        """
        This is method which return string with fields and values of the class
        :return:
        string
        """
        return f"number_of_cashier={self.number_of_cashier}," + \
            f"open_close_hours={self.open_close_hours}," + \
            f"max_number_of_people={self.max_number_of_people}," + \
            f"is_residential={self.is_residential}," + \
            f"year_of_building={self.year_of_building}"

    def __repr__(self):
        """
        This is representation method which return string with mame of class, fields and values
        :return:
        string
        """
        return f"Bank(number_of_cashier={self.number_of_cashier}," + \
            f"open_close_hours='{self.open_close_hours}'," + \
            f"max_number_of_people={self.max_number_of_people}," + \
            f"is_residential={self.is_residential}," + \
            f"year_of_building={self.year_of_building})"

    def calculate_construction_price(self):
        """
        calculates construction price of bank
        by multiplying maximum number of people
        and money equivalent and dividing them by number of cashier
        :return:
        float
            returns amount of money to build this bank
        """
        return self.max_number_of_people / self.number_of_cashier * self.money_equivalent
