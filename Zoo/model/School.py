from model.Building import Building


class School(Building):
    """
    Class school that have number of students, number of teachers which and name.
    """
    money_equivalent = 2500

    def __init__(self, number_of_students=0, number_of_teachers=0, name="No name",
                 is_residential=False, year_of_building=0):
        super().__init__(is_residential, year_of_building)
        self.number_of_students = number_of_students
        self.number_of_teachers = number_of_teachers
        self.name = name

    def __str__(self):
        return f"Number of students = {self.number_of_students}, \
               number of teachers = {self.number_of_teachers}, \
               name = {self.name}, \
               is residential = {self.is_residential}, \
               year of building = {self.year_of_building}"

    def __repr__(self):
        return f"School(Number of students = {self.number_of_students}, \
               number of teachers = {self.number_of_teachers}, \
               name = {self.name}, \
               is residential = {self.is_residential}, \
               year of building = {self.year_of_building})"

    def calculate_construction_price(self):
        """
        calculates construction price of school
        by multiplying number of students and money equivalent and dividing them by number of teachers
        :return:
        float
            returns amount of money to build this library
        """
        return self.number_of_students / self.number_of_teachers * self.money_equivalent
