class Person:
    def __init__(self, city_population: int, room_num: int):
        self._city_population = city_population
        self._room_num = room_num

    def get_person_room(self) -> int:
        return self._room_num

    def get_city_population(self) -> int:
        return self._city_population


if __name__ == "__main__":
    person = Person(100500, 42)
    print(person.get_person_room())
    print(person.get_city_population())
