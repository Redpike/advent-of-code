import numpy

_input = 4172


def get_power(x, y):
    rack = x + 10
    power = rack * y
    power += _input
    power *= rack
    return (power // 100 % 10) - 5


def get_power_2(x, y):
    rack = (x + 1) + 10
    power = rack * (y + 1)
    power += _input
    power *= rack
    return (power // 100 % 10) - 5


def get_fuel_cords():
    max_total_power = 0
    max_total_power_cords = (0, 0)
    for y in range(1, 300):
        for x in range(1, 300):
            total_power = sum(
                sum(get_power(x + square_x, y + square_y) for square_x in range(3)) for square_y in range(3))
            if total_power > max_total_power:
                max_total_power = total_power
                max_total_power_cords = (x, y)
    return ','.join(str(c) for c in max_total_power_cords)


def get_fuel_cords_and_size():
    grid = numpy.fromfunction(get_power_2, (300, 300))
    max_total_power = 0
    max_total_power_cords_size = (0, 0, 0)
    for y in range(300):
        for x in range(300):
            max_size = min([300 - y, 300 - x])
            for size in range(1, max_size + 1):
                total_power = numpy.sum(grid[x:x + size, y:y + size])
                if total_power > max_total_power:
                    max_total_power = total_power
                    max_total_power_cords_size = (x + 1, y + 1, size)
    return ','.join(str(c) for c in max_total_power_cords_size)


def main():
    print('Day 11 Part 1:', get_fuel_cords())
    print('Day 11 Part 2:', get_fuel_cords_and_size())


if __name__ == '__main__':
    main()
