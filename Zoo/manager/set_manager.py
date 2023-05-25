class set_manager:
    def __init__(self, building_manager):
        self.building_manager = building_manager
        self.purposes = []
        for b in building_manager.buildings:
            for p in b.purposes:
                self.purposes.append(p)
        self.building_manager_index = 0
        self.purpose_index = 0

    def __iter__(self):
        return self

    def __next__(self):
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
        return type(item), item

    def __str__(self):
        """
        This is method which return string with fields and values of the class
        :return:
        string
        """
        buildings = []
        for b in self.building_manager.buildings:
            buildings.append(b)
        return str(list(zip(buildings, self.purposes)))
