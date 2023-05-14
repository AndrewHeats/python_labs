from Zoo import Zoo

if __name__ == "__main__":
    zoos = [Zoo(49.4, 100, "Hoshin", "Tokyo"),
            Zoo(),
            Zoo.get_instance(),
            Zoo.get_instance()]
    for zoo in zoos:
        print(zoo.__repr__())
