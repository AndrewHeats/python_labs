class Zoo:
    """
    Class zoo that have name capacity, area, where it locates and name
    """

    def __init__(self, area, capacity, name, location):
        self.__area = area
        self.__capacity = capacity
        self.__name = name
        self.__location = location

    def __str__(self):
        return f"Area={self.__area}, capacity={self.__capacity}, name={self.__name}, location={self.__location}"

    def __repr__(self):
        return f"Zoo(Area={self.__area}, capacity={self.__capacity}, name={self.__name}, location={self.__location})"

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, new_area):
        self.__area = new_area
        return new_area

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, new_capacity):
        self.__capacity = new_capacity
        return new_capacity

    @property
    def name(self):
        return self.__area

    @name.setter
    def name(self, new_name):
        self.__name = new_name
        return new_name

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, new_location):
        self.__location = new_location
        return new_location

    def increase_capacity(self, capacity):
        """
        This method increases capacity and return the new value of it
        """
        self.__capacity += capacity
        return self.__capacity

    def split_area(self):
        """
        This method split area in a half and return the new value of it
        """
        self.__area /= 2
        return self.__area

    def add_new_region(self, area):
        """
        This method increases area of zoo and add a new region to location
        """
        self.__location += ", New Region"
        self.__area += area
        return self.__area
