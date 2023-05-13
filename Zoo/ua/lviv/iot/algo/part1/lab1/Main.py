from ua.lviv.iot.algo.part1.lab1.Zoo import Zoo

zoo = Zoo(49.4, 100, "Hoshin", "Tokyo")
print(zoo.area)
zoo.location = "Lviv"
zoo.split_area()
zoo.add_new_region(500.5)
zoo.increase_capacity(50)
print(zoo.__repr__())
