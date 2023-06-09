"""
This file is the main method which tests if this code compiling well
"""
from Zoo.exceptions.exceptions import ConstructionNotExisting, TooLittleSpace
from manager.building_manager import BuildingManager
from manager.set_manager import SetManager
from model.bank import Bank
from model.library import Library
from model.school import School
from model.zoo import Zoo

if __name__ == "__main__":
    buildings = []
    manager = BuildingManager(buildings)
    manager.add_building(Zoo(49.4, 10, "Hoshin", "Tokyo", 2004, True), message="building add succesfully")
    manager.add_building(Zoo(), message="building add succesfully")
    manager.add_building(Library(5, 2000, "Stepana bandery", 1980, False), message="building add succesfully")
    manager.add_building(Library(), message="building add succesfully")
    manager.add_building(School(500, 30, "LPML", 2000, True), message="building add succesfully")
    manager.add_building(School(), message="building add succesfully")
    manager.add_building(Bank(5, "9:00-18:00", 100, False, 2005), message="building add succesfully")
    manager.add_building(Bank(), message="building add succesfully")
    buildings_build_after_1999 = manager.find_buildings_build_after(1999)
    residential_buildings = manager.find_residential_buildings()

    for building in residential_buildings:
        print(building)
    print("\n")
    for building in buildings_build_after_1999:
        print(building)
    print("\n")
    print(list(manager.pairs_of_building_and_construction_price()))
    print(Zoo(49.4, 10, "Hoshin", "Tokyo", 2004, True).all_values_with_type(int))
    set_manager1 = SetManager(manager)
    ism = iter(set_manager1)
    for i in ism:
        print(ism.__next__())
    print(ism)
    print(manager.is_buildings_build_in(2000))
    print(manager.is_any_residential_building())
    exception_zoo = Zoo(0, 0)
    try:
        exception_zoo.calculate_construction_price()
    except ConstructionNotExisting as exc:
        print(exc)
    try:
        exception_zoo.increase_capacity(100)
    except TooLittleSpace as exc:
        print(exc)

