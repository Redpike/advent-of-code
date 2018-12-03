import re

test_input = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2'
]


def read_input():
    return open('input', 'r').read().split('\n')


def parse_input(_input: list):
    data = []
    for line in _input:
        numbers = [int(num) for num in re.findall(r'\d+', line)]
        data.append({'id': numbers[0], 'cords': [numbers[1], numbers[2]], 'dim': [numbers[3], numbers[4]]})
    return data


def get_cords(cords: list, dim: list):
    for x in range(dim[0]):
        for y in range(dim[1]):
            yield str(x + cords[0]) + ',' + str(y + cords[1])


def get_x_claims(_input: list):
    data = parse_input(_input)
    overlaps = set()
    filled = set()
    for line in data:
        for cords in get_cords(line['cords'], line['dim']):
            if cords in filled:
                overlaps.add(cords)
            else:
                filled.add(cords)
    return overlaps


def test():
    assert len(get_x_claims(test_input)) == 4


def main():
    test()
    _input = read_input()
    print('Day 03 Part 1:', len(get_x_claims(_input)))


if __name__ == '__main__':
    main()
