from itertools import cycle

dir_d = {'<': -1, '>': 1, '^': 1j, 'v': -1j}

test_input = [
    '/->-\\',
    '|   |  /----\\',
    '| /-+--+-\  |',
    '| | |  | v  |',
    '\-+-/  \-+--/',
    '\------/',
]

test_input_2 = [
    '/>-<\\',
    '|   |',
    '| /<+-\\',
    '| | | v',
    '\>+</ |',
    '  |   ^',
    '  \<->/',
]


def read_input():
    return open('input', 'r').read().splitlines()


def parse_data(_input: list):
    moves = {}
    carts = {}
    for i, line in enumerate(_input):
        for j, char in enumerate(line):
            location = j - i * 1j
            if char in r'/\+':
                moves[location] = char
            elif char in dir_d:
                carts[location] = dir_d[char], cycle([1j, 1, -1j])
    return moves, carts


def get_collisions(_input: list):
    moves, carts = parse_data(_input)
    collisions = []
    while len(carts) > 1:
        for location in sorted(carts, key=lambda x: (-x.imag, x.real)):
            if location not in carts:
                continue
            dxn, turn = carts.pop(location)
            location += dxn

            if location in carts:
                collisions.append(location)
                del carts[location]
                continue

            track = moves.get(location)
            if track == '+':
                dxn = dxn * next(turn)
            elif track is not None:
                dxn *= 1j * (2 * ((track == '/') ^ (dxn.real == 0)) - 1)
            carts[location] = dxn, turn
    return collisions, carts


def test():
    collisions, carts = get_collisions(test_input)
    collisions2, carts2 = get_collisions(test_input_2)
    assert collisions[0] == (7 - 3j)
    assert list(carts2.keys())[0] == (6 - 4j)


def main():
    test()
    _input = read_input()
    collisions, carts = get_collisions(_input)
    print('Day 13 Part 1:', collisions[0])
    print('Day 13 Part 2:', carts)


if __name__ == '__main__':
    main()
