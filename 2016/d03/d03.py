test_input = [5, 10, 25]


def read_input_file():
    input_lines = open('input', 'r').read().splitlines()
    sides = []
    for line in input_lines:
        x, y, z = line.split()
        sides.append([int(x), int(y), int(z)])
    return sides


def transpose_input_data(input_data):
    transposed_list = []

    for side in range(0, len(input_data), 3):
        [x, y, z] = zip(*[input_data[side], input_data[side + 1], input_data[side + 2]])
        transposed_list.append(list(x))
        transposed_list.append(list(y))
        transposed_list.append(list(z))
    return transposed_list


def is_possible_triangle(triangle: list):
    triangle.sort()
    if triangle[0] + triangle[1] > triangle[2]:
        return True
    else:
        return False


def get_possible_triangles(input_data):
    counter = 0
    for triangle in input_data:
        if is_possible_triangle(triangle):
            counter += 1
    return counter


def test():
    assert not is_possible_triangle(test_input)


def main():
    test()
    input_data = read_input_file()
    print('Day 03 Part 1:', get_possible_triangles(input_data))
    input_data = read_input_file()
    input_data = transpose_input_data(input_data)
    print('Day 03 Part 2:', get_possible_triangles(input_data))


if __name__ == '__main__':
    main()
