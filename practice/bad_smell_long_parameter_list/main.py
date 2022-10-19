from abc import ABC


class AbstractUnit(ABC):
    pass


class Field:
    def __init__(self):
        pass

    def set_unit(self, x_coord: int, y_coord: int, unit: AbstractUnit()):
        pass


class Unit(AbstractUnit):
    def __init__(self, state: str, speed: int, field: Field):
        self._state = state
        self._speed = speed
        self._field = field
        self._x_coord = 0
        self._y_coord = 0

    def move(self, direction):
        speed = self._get_speed()
        match direction:
            case 'UP':
                self._y = self._y_coord + speed
            case 'DOWN':
                self._y = self._y_coord - speed
            case 'LEFT':
                self._x = self._x_coord - speed
            case 'RIGHT':
                self._x = self._x_coord + speed
        self._field.set_unit(x_coord=self._x_coord, y_coord=self._y_coord, unit=self)

    def _get_speed(self) -> int:
        if self._state == 'fly':
            return round(self._speed * 1.2)
        elif self._state == 'crawl':
            return round(self._speed * 0.5)
        else:
            raise ValueError('Неизвестный зверь')


if __name__ == "__main__":
    field = Field()
    unit = Unit('fly', 1, field)
    unit.move('UP')
