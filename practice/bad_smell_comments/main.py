class Unit:
    def move(self, field, x_coord: int, y_coord: int, direction, is_fly: bool, is_crawl: bool, speed: int = 1):

        if is_fly and is_crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
        if is_crawl:
            speed *= 0.5
        match direction:
            case 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            case 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            case 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            case  'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed
