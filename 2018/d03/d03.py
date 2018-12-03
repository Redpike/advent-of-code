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


def no_overlaps(cords: list, dim: list, overlaps: set):
    for cords in get_cords(cords, dim):
        if cords in overlaps:
            return False
    return True


def get_id_of_no_overlaps(_input: list, overlaps: set):
    data = parse_input(_input)
    for line in data:
        if no_overlaps(line['cords'], line['dim'], overlaps):
            return line['id']


def test():
    overlaps = get_x_claims(test_input)
    assert len(overlaps) == 4
    assert get_id_of_no_overlaps(test_input, overlaps) == 3


def main():
    test()
    _input = read_input()
    overlaps = get_x_claims(_input)
    print('Day 03 Part 1:', len(overlaps))
    print('Day 03 Part 2:', get_id_of_no_overlaps(_input, overlaps))


if __name__ == '__main__':
    main()
