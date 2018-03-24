from collections import deque
from itertools import permutations

test_input = [
    '###########',
    '#0.1.....2#',
    '#.#######.#',
    '#4.......3#',
    '###########'
]

moves = {
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1)
}


def read_input_file():
    return open('input', 'r').read().splitlines()


def find_in_map(mp, predicate):
    return [(i, j) for i in range(len(mp)) for j in range(len(mp[i])) if predicate(mp[i][j])]


def bfs_from_to(mp, fr, to):
    q = deque([(0, fr)])
    vis = {fr}
    while q:
        dst, cur = q.pop()
        if cur == to:
            return dst
        y, x = cur
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if mp[ny][nx] != '#' and (ny, nx) not in vis:
                q.appendleft((dst + 1, (ny, nx)))
                vis.add((ny, nx))
    return -1


def get_fewest_number_of_steps(input_data: list, part_two=False):
    zero_pos = find_in_map(input_data, lambda x: x == '0')[0]
    nums_pos = find_in_map(input_data, lambda x: x in map(str, range(1, 10)))
    distance_from_0_to_others = [bfs_from_to(input_data, zero_pos, n_pos) for n_pos in nums_pos]
    amount_of_numbers = len(nums_pos)
    distances = [[None for _ in range(amount_of_numbers)] for _ in range(amount_of_numbers)]
    for i in range(amount_of_numbers):
        for j in range(i + 1, amount_of_numbers):
            distances[j][i] = distances[i][j] = bfs_from_to(input_data, nums_pos[i], nums_pos[j])
    steps, steps_2 = 999, 999
    for path in permutations(range(amount_of_numbers)):
        distance = distance_from_0_to_others[path[0]]
        for i in range(len(path) - 1):
            distance += distances[path[i]][path[i + 1]]
        steps = min(steps, distance)
        distance += distance_from_0_to_others[path[-1]]
        steps_2 = min(steps_2, distance)

    if part_two:
        return steps_2
    return steps


def test():
    assert get_fewest_number_of_steps(test_input) == 14


def main():
    test()
    input_data = read_input_file()
    print('Day 24 Part 1:', get_fewest_number_of_steps(input_data))
    print('Day 24 Part 1:', get_fewest_number_of_steps(input_data, part_two=True))


if __name__ == '__main__':
    main()
