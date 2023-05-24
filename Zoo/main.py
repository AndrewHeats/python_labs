"""
This file is the main method which tests if this code compiling well
"""
from manager.building_manager import BuildingManager
from model.bank import Bank
from model.library import Library
from model.school import School
from model.zoo import Zoo

if __name__ == "__main__":
    buildings = []
    manager = BuildingManager(buildings)
    manager.add_building(Zoo(49.4, 10, "Hoshin", "Tokyo", 2004, True))
    manager.add_building(Zoo())
    manager.add_building(Library(2000, 5, "Stepana bandery", 1980, False))
    manager.add_building(Library())
    manager.add_building(School(500, 30, "LPML", 2000, True))
    manager.add_building(School())
    manager.add_building(Bank(5, "9:00-18:00", 100, False, 2005))
    manager.add_building(Bank())
    buildings_build_after_1999 = manager.find_buildings_build_after(1999)
    residential_buildings = manager.find_residential_buildings()

    for building in residential_buildings:
        print(building)
    print("\n")
    for building in buildings_build_after_1999:
        print(building)
