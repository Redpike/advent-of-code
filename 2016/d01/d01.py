import re

test_input = [
    ['R2', 'L3'],
    ['R2', 'R2', 'R2'],
    ['R5', 'L5', 'R5', 'R3'],
    ['R8', 'R4', 'R4', 'R8']
]


directions = {
    'N': (0, 1),
    'S': (0, -1),
    'W': (-1, 0),
    'E': (1, 0)
}

regex_pattern = r'(R|L)(\d+)'


def read_input_file():
    return open('input', 'r').read().split(', ')


def set_new_direction(direction, turn):
    if direction == 'N':
        if turn == 'R':
            direction = 'E'
        elif turn == 'L':
            direction = 'W'
    elif direction == 'E':
        if turn == 'R':
            direction = 'S'
        elif turn == 'L':
            direction = 'N'
    elif direction == 'S':
        if turn == 'R':
            direction = 'W'
        elif turn == 'L':
            direction = 'E'
    elif direction == 'W':
        if turn == 'R':
            direction = 'N'
        elif turn == 'L':
            direction = 'S'
    else:
        raise ValueError

    return direction


def compute_blocks_away(input_data):
    position = (0, 0)
    direction = 'N'
    positions_list = [position]
    for sequence in input_data:
        regex_matcher = re.match(regex_pattern, sequence)
        turn = regex_matcher.group(1)
        number = int(regex_matcher.group(2))
        direction = set_new_direction(direction, turn)
        dx = number * int(directions[direction][0]) if directions[direction][0] != 0 else 0
        dy = number * int(directions[direction][1]) if directions[direction][1] != 0 else 0
        position = (position[0] + dx, position[1] + dy)
        positions_list.append(position)
    # Manhattan distance
    x_diff = abs(positions_list[-1][0] - positions_list[0][0])
    y_diff = abs(positions_list[-1][1] - positions_list[0][1])
    return x_diff + y_diff


def compute_blocks_away_part_2(input_data):
    position = (0, 0)
    direction = 'N'
    positions_list = [position]
    for sequence in input_data:
        regex_matcher = re.match(regex_pattern, sequence)
        turn = regex_matcher.group(1)
        number = int(regex_matcher.group(2))
        direction = set_new_direction(direction, turn)
        for i in range(1, number + 1):
            position = (position[0] + int(directions[direction][0]), position[1] + int(directions[direction][1]))
            if position not in positions_list:
                positions_list.append(position)
            else:
                # Manhattan distance
                x_diff = abs(position[0] - positions_list[0][0])
                y_diff = abs(position[1] - positions_list[0][1])
                return x_diff + y_diff


def test():
    assert compute_blocks_away(test_input[0]) == 5
    assert compute_blocks_away(test_input[1]) == 2
    assert compute_blocks_away(test_input[2]) == 12
    assert compute_blocks_away_part_2(test_input[3]) == 4


def main():
    test()
    input_data = read_input_file()
    print('Day 01 Part 1:', compute_blocks_away(input_data))
    print('Day 01 Part 2:', compute_blocks_away_part_2(input_data))


if __name__ == '__main__':
    main()
