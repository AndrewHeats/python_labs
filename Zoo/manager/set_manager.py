"""
this is set manager file
"""


class SetManager:
    """
    A class that represents a set manager.
    """

    def __init__(self, building_manager):
        """
        Initializes a set_manager object.

        :param building_manager: An instance of the building_manager class.
        """
        self.building_manager = building_manager
        self.purposes = [purpose for building in self.building_manager.buildings for purpose in building.purposes]
        self.building_manager_index = 0
        self.purpose_index = 0

    def __iter__(self):
        """
        Returns an iterator object.

        :return: An iterator object.
        """
        return self

    def __next__(self):
        """
        Returns the next value from the iterator.

        :return: The next value from the iterator.
        :raises StopIteration: If there are no more values to iterate over.
        """
        if IndexError:
            raise StopIteration
        if self.building_manager_index > len(self.building_manager.buildings):
            self.purpose_index = 0
            self.building_manager_index += 1
        self.purpose_index += 1
        purpose = self.purposes[self.purpose_index - 1]
        return purpose

    def __getitem__(self, index):
        """
        Returns the value at the specified index.

        :param index: The index of the value to retrieve.
        :return: The value at the specified index.
        :raises IndexError: If the index is out of range.
        """
        return self.purposes[index]

    def __str__(self):
        """
        Returns a string representation of the class with fields and values.

        :return: A string representation of the class.
        """
        buildings = [building for building in self.building_manager.buildings]
        return str(list(zip(buildings, self.purposes)))
