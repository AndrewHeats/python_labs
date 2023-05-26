"""
this is set manager file
"""


class set_manager:
    """
    A class that represents a set manager.
    """

    def __init__(self, building_manager):
        """
        Initializes a set_manager object.

        :param building_manager: An instance of the building_manager class.
        """
        self.building_manager = building_manager
        self.purposes = []
        for b in building_manager.buildings:
            for p in b.purposes:
                self.purposes.append(p)
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
        if self.purpose_index >= len(self.purposes):
            if self.building_manager_index >= len(self.building_manager.buildings):
                raise StopIteration
            else:
                self.purpose_index = 0
                self.building_manager_index += 1
        else:
            self.purpose_index += 1
            return self.purposes[self.purpose_index - 1]

    def __getitem__(self, item):
        """
        Returns the type and value of the given item.

        :param item: The item to get type and value for.
        :return: A tuple containing the type and value of the item.
        """
        return type(item), item

    def __str__(self):
        """
        Returns a string representation of the class with fields and values.

        :return: A string representation of the class.
        """
        buildings = []
        for b in self.building_manager.buildings:
            buildings.append(b)
        return str(list(zip(buildings, self.purposes)))
