from model.Building import Building


class Library(Building):
    """
    Class library that have number of halls, number of books which are held there and address.
    """
    money_equivalent = 500

    def __init__(self, number_of_halls=0, number_of_books=0, address="Nowhere",
                 year_of_building=0, is_residential=False):
        super().__init__(year_of_building, is_residential)
        self.number_of_halls = number_of_halls
        self.number_of_books = number_of_books
        self.address = address

    def __str__(self):
        return f"Number of halls = {self.number_of_halls}, \
               number of books = {self.number_of_books}, \
               address = {self.address}, \
               is residential = {self.is_residential}, \
               year of building = {self.year_of_building}"

    def __repr__(self):
        return f"Library(Number of halls = {self.number_of_halls}, \
              number of books = {self.number_of_books}, \
              address = {self.address}, \
              is residential = {self.is_residential}, \
              year of building = {self.year_of_building})"

    def calculate_construction_price(self):
        """
        calculates construction price of library
        by multiplying number of books and money equivalent and dividing them by number of halls
        :return:
        float
            returns amount of money to build this library
        """
        return self.number_of_books / self.number_of_halls * self.money_equivalent
