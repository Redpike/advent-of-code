from collections import defaultdict

test_input = [
    '>',
    '^>v<',
    '^v^v^v^v^v'
]


moves = {
    '>': (1, 0),
    'v': (0, -1),
    '<': (-1, 0),
    '^': (0, 1)
}


def readInputFile():
    input_file = open('input', 'r')
    input_data = input_file.readline()
    return input_data


def countHouses(input_data):
    visited = defaultdict(int)
    curr_position = (0, 0)

    for move in input_data:
        visited[curr_position] = visited[curr_position]
        move_cords = moves.get(move)
        curr_position = (curr_position[0] + move_cords[0], curr_position[1] + move_cords[1])

    return len(visited)


def countHousesWithRobot(input_data):
    visited = defaultdict(int)
    santa_curr_position = (0, 0)
    robo_curr_position = (0, 0)
    visited[santa_curr_position] = 0
    counter = 0

    for move in input_data:
        move_cords = moves.get(move)

        if counter % 2 == 0:
            santa_curr_position = (santa_curr_position[0] + move_cords[0], santa_curr_position[1] + move_cords[1])
            visited[santa_curr_position] = visited[santa_curr_position]
        else:
            robo_curr_position = (robo_curr_position[0] + move_cords[0], robo_curr_position[1] + move_cords[1])
            visited[robo_curr_position] = visited[robo_curr_position]
        counter += 1

    return len(visited)


def test():
    assert countHouses(test_input[0]) == 1
    assert countHouses(test_input[1]) == 4
    assert countHouses(test_input[2]) == 2


def main():
    test()
    input_data = readInputFile()
    print('Day 03 Part 1:', countHouses(input_data))
    print('Day 03 Part 2:', countHousesWithRobot(input_data))


if __name__ == '__main__':
    main()
