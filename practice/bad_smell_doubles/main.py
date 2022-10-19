class SomeClass:
    def __init__(self):
        self._list = [3, 2, 1, 4, 2, 1]

    def sorted_func(self, reverse: bool = False) -> list:
        return sorted(self._list, reverse=reverse)


if __name__ == "__main__":
    some_inst = SomeClass()
    print(some_inst.sorted_func(True))
