class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return self.x * self.y * self.z


class CubeVolumeCalculator:
    @staticmethod
    def calc_cube_volume(cube):
        return cube.get_volume()


if __name__ == "__main__":
    cube = Cube(10, 10, 10)
    cvm = CubeVolumeCalculator()
    print(cvm.calc_cube_volume(cube))
