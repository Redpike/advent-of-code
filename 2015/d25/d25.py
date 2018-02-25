test_input = (6, 6)
input_data = (3010, 3019)
first_code = 20151125


def generate_index(_input: tuple):
    triangle = (_input[0] + _input[1] - 1) * (_input[0] + _input[1]) / 2
    return triangle - _input[0]


def generate_code(_input: tuple):
    code = first_code
    target_index = int(generate_index(_input))
    for i in range(target_index):
        code = (code * 252533) % 33554393
    return code


def test():
    assert generate_code(test_input) == 27995004


def main():
    test()
    print('Day 25 Part 1:', generate_code(input_data))


if __name__ == '__main__':
    main()
