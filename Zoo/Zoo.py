class Zoo:
    """
    Class zoo that have name capacity, area, where it locates and name.

    """
    instance = None

    def __init__(self, area=0, capacity=0, name="noname", location="nowhere"):
        self.area = area
        self.capacity = capacity
        self.name = name
        self.location = location

    def __str__(self):
        return f"Area={self.area}, \
        capacity={self.capacity}, \
        name={self.name}, \
        location={self.location}"

    def __repr__(self):
        return f"Zoo(Area={self.area}, \
        capacity={self.capacity}, \
        name={self.name}, \
        location={self.location})"

    def __cmp__(self, other):
        return self.area == other.area \
            and self.capacity == other.capacity and \
            self.location == other.location and \
            self.name == other.name

    @staticmethod
    def get_instance():
        """
        Returns the singleton instance of the Zoo class.
        If no instance exists, a new instance is created.
        Returns:
        --------
        Zoo
            The singleton instance of the Zoo class.
        """
        if not Zoo.instance:
            Zoo.instance = Zoo()
        return Zoo.instance

    def increase_capacity(self, capacity):
        """
        This method increases capacity and return the new value of it
        :return
        int
            returns new capacity value
        """
        self.capacity += capacity
        return self.capacity

    def split_area(self):
        """
        This method split area in a half and return the new value of it
        :return
        float
            returns new area value
        """
        self.area /= 2
        return self.area

    def add_new_region(self, area):
        """
        This method increases area of zoo and add a new region to location
        :return
        float
            returns new area value
        """
        self.location += ", New Region"
        self.area += area
        return self.area

