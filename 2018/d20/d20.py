from collections import *

directions = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}


def read_input():
    return open('input', 'r').readline()


def solve(input_data: str, part: int):
    positions = []
    x, y = 5000, 5000
    regular_map = defaultdict(set)
    prev_x, prev_y = x, y
    distances = defaultdict(int)
    for char in input_data[1:-1]:
        if char == "(":
            positions.append((x, y))
        elif char == ")":
            x, y = positions.pop()
        elif char == "|":
            x, y = positions[-1]
        else:
            dx, dy = directions[char]
            x += dx
            y += dy
            regular_map[(x, y)].add((prev_x, prev_y))
            if distances[(x, y)] != 0:
                distances[(x, y)] = min(distances[(x, y)], distances[(prev_x, prev_y)] + 1)
            else:
                distances[(x, y)] = distances[(prev_x, prev_y)] + 1

        prev_x, prev_y = x, y

    if part == 1:
        return max(distances.values())
    else:
        return len([x for x in distances.values() if x >= 1000])


def main():
    input_data = read_input()
    print('Day 20 Part 1:', solve(input_data, part=1))
    print('Day 20 Part 1:', solve(input_data, part=2))


if __name__ == '__main__':
    main()
