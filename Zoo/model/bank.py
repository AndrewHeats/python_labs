from model.building import Building


class Bank(Building):
    """
    Class bank that have number of cashier who working there, maximum number of people and open-close hours.
    """
    money_equivalent = 3000

    def __init__(self, number_of_cashier=0, open_close_hours="00:00-00:00", max_number_of_people=0,
                 is_residential=False, year_of_building=0):
        super().__init__(is_residential, year_of_building)
        self.number_of_cashier = number_of_cashier
        self.open_close_hours = open_close_hours
        self.max_number_of_people = max_number_of_people

    def __str__(self):
        return f"number_of_cashier={self.number_of_cashier}, \
        open_close_hours='{self.open_close_hours}', \
        max_number_of_people={self.max_number_of_people}, \
        is_residential={self.is_residential}, \
        year_of_building={self.year_of_building}"

    def __repr__(self):
        return f"Bank(number_of_cashier={self.number_of_cashier}, \
        open_close_hours='{self.open_close_hours}', \
        max_number_of_people={self.max_number_of_people}, \
        is_residential={self.is_residential}, \
        year_of_building={self.year_of_building})"

    def calculate_construction_price(self):
        """
        calculates construction price of bank
        by multiplying maximum number of people and money equivalent and dividing them by number of cashier
        :return:
        float
            returns amount of money to build this bank
        """
        return self.max_number_of_people / self.number_of_cashier * self.money_equivalent
