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
    purposes = {'educational', 'socialising', 'personal development'}

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
        calculates construction price of school
        by multiplying number of students and money equivalent and dividing them by number of teachers
        :return:
        int
            returns amount of money to build this library
        """
        if not self.number_of_teachers:
            return 0
        return int(self.number_of_students / self.number_of_teachers * self.money_equivalent)
