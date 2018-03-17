from hashlib import md5
from itertools import compress

test_input = [
    'ihgpwlah',
    'kglvqrro',
    'ulqzkmiv'
]

input_data = 'dmypynyp'

moves = {
    'U': lambda x, y: (x, y - 1),
    'D': lambda x, y: (x, y + 1),
    'L': lambda x, y: (x - 1, y),
    'R': lambda x, y: (x + 1, y)
}


def doors(_input:str, path: list):
    string = (_input + ''.join(path)).encode()
    return (int(x, 16) > 10 for x in md5(string).hexdigest()[:4])


def bfs(_input: str, start: tuple, goal: tuple):
    queue = [(start, [start], [])]
    while queue:
        (x, y), path, dirs = queue.pop(0)
        for direction in compress('UDLR', doors(_input, dirs)):
            next_move = moves[direction](x, y)
            nx, ny = next_move
            if not (0 <= nx < 4 and 0 <= ny < 4):
                continue
            elif next_move == goal:
                yield dirs + [direction]
            else:
                queue.append((next_move, path + [next_move], dirs + [direction]))


def get_shortest_path(_input: str, part: int):
    paths = list(bfs(_input, (0, 0), (3, 3)))
    if part == 1:
        return ''.join(paths[0])
    elif part == 2:
        return len(paths[-1])


def test():
    assert get_shortest_path(test_input[0], part=1) == 'DDRRRD'
    assert get_shortest_path(test_input[1], part=1) == 'DDUDRLRRUDRD'
    assert get_shortest_path(test_input[2], part=1) == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'
    assert get_shortest_path(test_input[0], part=2) == 370
    assert get_shortest_path(test_input[1], part=2) == 492
    assert get_shortest_path(test_input[2], part=2) == 830


def main():
    test()
    print('Day 17 Part 1:', get_shortest_path(input_data, part=1))
    print('Day 17 Part 2:', get_shortest_path(input_data, part=2))


if __name__ == '__main__':
    main()
