test_input = [
    ['ne', 'ne', 'ne'],
    ['ne', 'ne', 'sw', 'sw'],
    ['ne', 'ne', 's', 's'],
    ['se', 'sw', 'se', 'sw', 'sw']
]


moves = {
    'n': (1, 0),
    'ne': (0, -1),
    'nw': (1, 1),
    's': (-1, 0),
    'se': (-1, -1),
    'sw': (0, 1)
}


distances = []


def readInputFile():
    input_file = open('input', 'r')
    input_data = []
    for line in input_file:
        input_data = line.strip().split(',')
        input_data = [str(x) for x in input_data]
    return input_data


def computeDistance(starting_point, point):
    delta_x = point[0] - starting_point[0]
    delta_y = point[1] - starting_point[1]
    delta_xy = delta_y - delta_x
    return max(abs(delta_x), abs(delta_y), abs(delta_xy))


def getDistanceFromStartingPointToLast(input_data):
    global distances
    distances = list()
    starting_point, point = (0, 0), (0, 0)
    for move in input_data:
        point = (point[0] + moves[move][0], point[1] + moves[move][1])
        distances.append(computeDistance(starting_point, point))


def test():
    getDistanceFromStartingPointToLast(test_input[0])
    assert distances[-1] == 3
    getDistanceFromStartingPointToLast(test_input[1])
    assert distances[-1] == 0
    getDistanceFromStartingPointToLast(test_input[2])
    assert distances[-1] == 2
    getDistanceFromStartingPointToLast(test_input[3])
    assert distances[-1] == 3


def main():
    test()
    input_data = readInputFile()
    getDistanceFromStartingPointToLast(input_data)
    print('Day 11 Part 1:', distances[-1])
    print('Day 11 Part 2:', max(distances))


if __name__ == '__main__':
    main()
