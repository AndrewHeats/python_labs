from abc import ABC, abstractmethod


class Building(ABC):
    def __init__(self, year_of_building=0, is_residential=False):
        self.year_of_building = year_of_building
        self.is_residential = is_residential
        super().__init__()

    @abstractmethod
    def calculate_construction_price(self):
        pass

    def __str__(self):
        return f"Building(year_of_building={self.year_of_building},\
         is_residential={self.is_residential})"

    def __repr__(self):
        return f"Building(year_of_building={self.year_of_building},\
         is_residential={self.is_residential})"