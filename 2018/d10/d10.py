import re

test_input = [
    'position=< 9,  1> velocity=< 0,  2>',
    'position=< 7,  0> velocity=<-1,  0>',
    'position=< 3, -2> velocity=<-1,  1>',
    'position=< 6, 10> velocity=<-2, -1>',
    'position=< 2, -4> velocity=< 2,  2>',
    'position=<-6, 10> velocity=< 2, -2>',
    'position=< 1,  8> velocity=< 1, -1>',
    'position=< 1,  7> velocity=< 1,  0>',
    'position=<-3, 11> velocity=< 1, -2>',
    'position=< 7,  6> velocity=<-1, -1>',
    'position=<-2,  3> velocity=< 1,  0>',
    'position=<-4,  3> velocity=< 2,  0>',
    'position=<10, -3> velocity=<-1,  1>',
    'position=< 5, 11> velocity=< 1, -2>',
    'position=< 4,  7> velocity=< 0, -1>',
    'position=< 8, -2> velocity=< 0,  1>',
    'position=<15,  0> velocity=<-2,  0>',
    'position=< 1,  6> velocity=< 1,  0>',
    'position=< 8,  9> velocity=< 0, -1>',
    'position=< 3,  3> velocity=<-1,  1>',
    'position=< 0,  5> velocity=< 0, -1>',
    'position=<-2,  2> velocity=< 2,  0>',
    'position=< 5, -2> velocity=< 1,  2>',
    'position=< 1,  4> velocity=< 2,  1>',
    'position=<-2,  7> velocity=< 2, -2>',
    'position=< 3,  6> velocity=<-1, -1>',
    'position=< 5,  0> velocity=< 1,  0>',
    'position=<-6,  0> velocity=< 2,  0>',
    'position=< 5,  9> velocity=< 1, -2>',
    'position=<14,  7> velocity=<-2,  0>',
    'position=<-3,  6> velocity=< 2, -1>'
]

regex_pattern = r'-?\d+'


def read_input():
    return open('input', 'r').read().splitlines()


def parse_input(_input: list):
    input_numbers = []
    for line in _input:
        x, y, vx, vy = re.findall(regex_pattern, line)
        input_numbers.append([int(x), int(y), int(vx), int(vy)])
    return input_numbers


def get_message(_input: list):
    input_numbers = parse_input(_input)
    for t in range(100_000):
        min_x = min([x for x, y, _, _ in input_numbers])
        max_x = max([x for x, y, _, _ in input_numbers])
        min_y = min([y for x, y, _, _ in input_numbers])
        max_y = max([y for x, y, _, _ in input_numbers])
        size_of_matrix = 100

        if min_x + size_of_matrix >= max_x and min_y + size_of_matrix >= max_y:
            print('Seconds:', t)
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    if (x, y) in [(px, py) for px, py, _, _ in input_numbers]:
                        print('#', end='')
                    else:
                        print('.', end='')
                print()
        for line in input_numbers:
            line[0] += line[2]
            line[1] += line[3]


def test():
    get_message(test_input)


def main():
    test()
    _input = read_input()
    print('Day 10 Part 1:', get_message(_input))


if __name__ == '__main__':
    main()
