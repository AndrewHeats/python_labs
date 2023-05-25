"""
This file is the main method which tests if this code compiling well
"""
from manager.building_manager import BuildingManager
from manager.set_manager import set_manager
from model.bank import Bank
from model.library import Library
from model.school import School
from model.zoo import Zoo

if __name__ == "__main__":
    manager = BuildingManager()
    manager.add_building(Zoo(49.4, 10, "Hoshin", "Tokyo", 2004, True))
    manager.add_building(Zoo())
    manager.add_building(Library(5, 2000, "Stepana bandery", 1980, False))
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
    print("\n")
    print(list(manager.pairs_of_building_and_construction_price()))
    '''print(Zoo(49.4, 10, "Hoshin", "Tokyo", 2004, True).all_values_with_type(int))
    set_manager1 = set_manager(manager)
    ism = iter(set_manager1)
    for i in ism:
        print(i)
    '''
    print(manager.is_buildings_build_in(2000))
    print(manager.is_any_residential_building())
    i = 0
    manager.some_method(i)