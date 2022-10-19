class Foo:
    @staticmethod
    def _read(csv: str) -> dict:
        return [line.split(';') for line in csv.split('\n')]

    @staticmethod
    def _sort(data: dict) -> dict:
        return sorted(data, key=lambda x: int(x[1]))

    @staticmethod
    def _filter(data: dict) -> dict:
        return [x for x in data if int(x[1]) >= 10]

    def get_users_list(self, csv: str) -> dict:
        data = self._read(csv)
        data = self._sort(data)
        return self._filter(data)


if __name__ == "__main__":
    csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""
    foo = Foo()
    print(foo.get_users_list(csv))
