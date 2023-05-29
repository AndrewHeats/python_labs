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
    purposes = {'financial', 'safekeeping', 'payment and transaction processing'}

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
        return str(f"{self.__dict__}")

    def __repr__(self):
        """
        This is representation method which return string with mame of class, fields and values
        :return:
        string
        """
        return str(f"{self.__class__.__name__}: {self.__dict__}")

    def calculate_construction_price(self):
        """
        calculates construction price of bank
        by multiplying maximum number of people
        and money equivalent and dividing them by number of cashier
        :return:
        int
            returns amount of money to build this bank
        """
        if not self.number_of_cashier:
            return 0
        return int(self.max_number_of_people / self.number_of_cashier * self.money_equivalent)
