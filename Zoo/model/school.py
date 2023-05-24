"""
This is file which have school class
"""



from .building import Building
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=relative-beyond-top-level
class School(Building):
    """
    Class school that have number of students, number of teachers which and name.
    """
    money_equivalent = 2500

    def __init__(self, number_of_students=0, number_of_teachers=0, name="No name",
                 is_residential=False, year_of_building=0):
        self.number_of_students = number_of_students
        self.number_of_teachers = number_of_teachers
        self.name = name
        super().__init__(is_residential, year_of_building)

    def __str__(self):
        """
        This is method which return string with fields and values of the class
        :return:
        string
        """
        return f"Number of students = {self.number_of_students}, " + \
            f"number of teachers = {self.number_of_teachers}, " + \
            f"name = {self.name}, " + \
            f"is residential = {self.is_residential}, " + \
            f"year of building = {self.year_of_building} "

    def __repr__(self):
        """
        This is representation method which return string with mame of class, fields and values
        :return:
        string
        """
        return f"School(Number of students = {self.number_of_students}," + \
            f"number of teachers = {self.number_of_teachers}," + \
            f"name = {self.name}," + \
            f"is residential = {self.is_residential}," + \
            f"year of building = {self.year_of_building})"

    def calculate_construction_price(self):
        """
        calculates construction price of school
        by multiplying number of students and money equivalent and dividing them by number of teachers
        :return:
        float
            returns amount of money to build this library
        """
        return self.number_of_students / self.number_of_teachers * self.money_equivalent
