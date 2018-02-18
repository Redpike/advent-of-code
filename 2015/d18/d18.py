import numpy

test_input = numpy.array([
    [0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 0]
])

test_input2 = numpy.array([
    [1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1]
])


def read_input_file():
    return open('input', 'r').read().splitlines()


def convert_data(input_data):
    converted_data = [[int(element) for element in line.strip().replace(
        '#', '1').replace('.', '0')] for line in input_data]
    return numpy.array(converted_data)


def update_grid(grid, part):
    new_grid = numpy.zeros(grid.shape)
    for i in range(grid.shape[0]):
        i_min = max(0, i - 1)
        i_max = min(i + 1, grid.shape[0])
        for j in range(grid.shape[1]):
            old_value = grid[i, j]
            j_min = max(0, j - 1)
            j_max = min(j + 1, grid.shape[1])
            on_neighbs = grid[i_min:i_max + 1, j_min:j_max + 1].sum() - old_value
            if old_value == 1:
                new_grid[i, j] = int(on_neighbs in [2, 3])
            else:
                new_grid[i, j] = int(on_neighbs == 3)
        if part == 2:
            new_grid[0, 0] = 1
            new_grid[0, grid.shape[1] - 1] = 1
            new_grid[grid.shape[0] - 1, 0] = 1
            new_grid[grid.shape[0] - 1, grid.shape[1] - 1] = 1
    return new_grid


def get_on_lights(grid, steps, part):
    for i in range(steps):
        grid = update_grid(grid, part)
    return int(grid.sum())


def test():
    assert get_on_lights(test_input, 4, 1) == 4
    assert get_on_lights(test_input2, 5, 2) == 17


def main():
    test()
    input_data = read_input_file()
    converted_data = convert_data(input_data)
    print('Day 18 Part 1:', get_on_lights(converted_data, 100, 1))
    print('Day 18 Part 2:', get_on_lights(converted_data, 100, 2))


if __name__ == '__main__':
    main()
